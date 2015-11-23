import random
from randomGraph import *
from operator import itemgetter

def maxBandwidth_Dijkstra(B,s,t):
	status = ["unseen"]*5000
	dad = [-1]*5000
	capacity = [0]*5000
	status[s] = "in-tree"
	for w in B[s][1]:
		status[w[1]] = "fringe"
		capacity[w[1]] = w[0]
		dad[w[1]] = s
	while("fringe" in status):
		v = largestFringe(status,capacity)
		status[v] = "in-tree"
		for w in B[v][1]:
			if status[w[1]]=="unseen":
				status[w[1]] = "fringe"
				dad[w[1]] = v
				capacity[w[1]] = minimum(capacity[v],w[0])
			elif(status[w[1]]=="fringe" and capacity[w[1]]<minimum(capacity[v],w[0])):
				dad[w[1]] = v
				capacity[w[1]] = minimum(capacity[v],w[0])
	#return dad
	i = t
	path = [t]
	while(dad[i]!=-1):
		path.append(dad[i])
		i = dad[i]
	path.reverse()
	bandwidth = 1000
	for i in range(len(path)-1):
		v = path[i]
		u = path[i+1]
		for x in B.keys():
			if x==v:
				for y in B[v][1]:
					if y[1]==u:
						if bandwidth>y[0]:
							bandwidth = y[0]
	print "Number of vertices traversed in maximum bandwidth path is : " + str(len(path)),"with bandwidth:",bandwidth
	print path
				
				
def minimum(a,b):
	if(a<b):
		return a
	else:
		return b
		
def largestFringe(status,capacity):
	temp = -1
	v = -1
	vertex = []
	for i in range(len(status)):
		if status[i]=="fringe":
			vertex.append(i)
	#arr = []
	for i in vertex:
	#	arr.append((capacity[i],i))
	#arr = sorted(arr,key=itemgetter(0))
		if temp<capacity[i]:
			temp = capacity[i]
			v = i
	return v
	#last = arr[-1]
	#v = last[1]
	#return v
	
#B,s,t = undirectedRandomGraph(5000,1000)
#maxBandwidth(B,s,t)