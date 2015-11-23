import sys
import random
from heapImplementation import *
from randomGraph import *
from time import clock

def maxBandwidth_DijkstraHeap(B,s,t):
	status = ["unseen"]*5000
	dad = [-1]*5000
	capacity = [0]*5000
	status[s] = "in-tree"
	for w in B[s][1]:
		status[w[1]] = "fringe"
		capacity[w[1]] = w[0]
		dad[w[1]] = s
	unvisited_queue = []
	for v in B.keys():
		if status[v]=="in-tree":
			for pair in B[v][1]:
				if status[pair[1]]=="fringe":
					unvisited_queue.append((capacity[pair[1]],pair[1]))
	heapify_max(unvisited_queue)
	while(len(unvisited_queue)):
		uv = heappop(unvisited_queue)
		v = uv[1]
		status[v] = "in-tree"
		for w in B[v][1]:
			if status[w[1]]=="unseen":
				status[w[1]] = "fringe"
				dad[w[1]] = v
				capacity[w[1]] = minimum(capacity[v],w[0])
				heappush(unvisited_queue,(capacity[w[1]],w[1]))
			elif(status[w[1]]=="fringe" and capacity[w[1]]<minimum(capacity[v],w[0])):
				dad[w[1]] = v
				old = capacity[w[1]]
				capacity[w[1]] = minimum(capacity[v],w[0])
				update(unvisited_queue,(capacity[w[1]],w[1]),(old,w[1]))
		#while(len(unvisited_queue)):
		#	heappop(unvisited_queue)
		""""unvisited_queue = []
		for v in B.keys():
			if status[v]=="in-tree":
				for pair in B[v][1]:
					if status[pair[1]]=="fringe":
						unvisited_queue.append(pair)
		heapify_max(unvisited_queue)"""
	#return dad
	i = t
	path = [t]
	while(dad[i]!=-1):
		path.append(dad[i])
		i = dad[i]
	path.reverse()
	bandwidth = 1001
	for i in range(len(path)-1):
		v = path[i]
		u = path[i+1]
		for x in B.keys():
			if x==v:
				for y in B[v][1]:
					if y[1]==u:
						if bandwidth>y[0]:
							bandwidth = y[0]
	print "Number of vertices traversed in maximum bandwidth path is : " + str(len(path)), "with bandwidth: ", bandwidth
	print path
				
				
def minimum(a,b):
	if(a<b):
		return a
	else:
		return b

	
"""B,s,t = undirectedRandomGraph(5000,20)
start = clock()
maxBandwidth_DijkstraHeap(B,s,t)
stop = clock()"""