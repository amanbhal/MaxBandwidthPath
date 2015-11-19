from randomSparseGraph import *
#from maxBWP_dijkstra import *
from maxBWP_dijkstra_heap import *
from maxBWP_kruskal import *
from time import clock
from dijkstra_slow import *
B,s,t = undirectedSparseRandomGraph(500)
start = clock()
maxBandwidth_Dijkstra(B,s,t)
dijkstra_stop = clock()
maxBandwidth_DijkstraHeap(B,s,t)
dijkstraHeap_stop = clock()
maxBandwidth_Kruskal(B,s,t,500)
kruskal_stop = clock()
time = {}
time.update({"dijkstra" : (dijkstra_stop-start)})
time.update({"dijkstraHeap" : (dijkstraHeap_stop-dijkstra_stop)})
time.update({"kruskal" : (kruskal_stop-dijkstraHeap_stop)})
for i in sorted(time,key=time.__getitem__):
	print i,time[i]