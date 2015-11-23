from randomSparseGraph import *
from maxBWP_dijkstra import *
from dijkstra_heap_fast import *
from time import clock
#from dijkstra_slow import *
from kruskal_ultra_fast import *
for i in range(5):
	print "---------------------ITERATION "+str(i)+"------------------------------------"
	B,s,t = undirectedSparseRandomGraph(5000)
	print "Starting Point: ",s,"Ending Point:",t
	start = clock()
	maxBandwidth_Dijkstra(B,s,t)
	dijkstra_stop = clock()
	maxBandwidth_DijkstraHeap(B,s,t)
	dijkstraHeap_stop = clock()
	#maxBandwidth_Kruskal(B,s,t,500)
	#kruskal_stop = clock()
	maxBandwidth_Kruskal_Fast(B,s,t,5000)
	kruskal_fast_stop = clock()
	time = {}
	time.update({"dijkstra" : (dijkstra_stop-start)})
	time.update({"dijkstraHeap" : (dijkstraHeap_stop-dijkstra_stop)})
	#time.update({"kruskal" : (kruskal_stop-dijkstraHeap_stop)})
	time.update({"kruskal_fast" : (kruskal_fast_stop-dijkstraHeap_stop)})
	for i in sorted(time,key=time.__getitem__):
		print i,time[i]