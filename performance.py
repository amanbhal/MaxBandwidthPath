from randomGraph import *
from maxBWP_dijkstra import *
from dijkstra_heap_fast import *
from time import clock
from kruskal_ultra_fast import *
B,s,t = undirectedRandomGraph(5000,20)
start = clock()
maxBandwidth_Dijkstra(B,s,t)
dijkstra_stop = clock()
maxBandwidth_DijkstraHeap(B,s,t)
dijkstraHeap_stop = clock()
maxBandwidth_Kruskal_Fast(B,s,t,5000)
kruskal_fast_stop = clock()
time = {}
time.update({"dijkstra" : (dijkstra_stop-start)})
time.update({"dijkstraHeap" : (dijkstraHeap_stop-dijkstra_stop)})
#time.update({"kruskal" : (kruskal_stop-dijkstraHeap_stop)})
#time.update({"kruskal_fast" : (kruskal_fast_stop-kruskal_stop)})
time.update({"kruskal_fast" : (kruskal_fast_stop-dijkstraHeap_stop)})
for i in sorted(time,key=time.__getitem__):
	print i,time[i]