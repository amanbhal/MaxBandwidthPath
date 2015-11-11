import sys
import heapq
import profile
import random
import timeit
import time
from datetime import datetime
from heapImplementation import *

def randomGraph():
	#start = timeit.default_timer()
	#start = datetime.now().microsecond
	##start = time.time()
	B = {}
	A = []
	for i in range(5000):
		A.append(i)
		B.update({i:[]})
		
	for i in range(5000):
		start = random.randrange(0,4994)
		A.pop(A.index(i))
		random.shuffle(A)
		for j in A[start:start+6]:
			B[i].append((random.randrange(1,101),j))
		A.append(i)
	#stop = timeit.default_timer()
	#stop = datetime.now().microsecond
	##print (time.time() - start)
	s = A[random.randrange(0,5000,2)]
	t = A[random.randrange(1,5000,2)]
	print "Starting Point is : " + str(s)
	print "Ending Point is : " + str(t)
	maxBandwidth(B,s,t)

def maxBandwidth(B,s,t):
	status = ["unseen"]*5000
	dad = [-1]*5000
	capacity = [0]*5000
	status[s] = "in-tree"
	for w in B[s]:
		status[w[1]] = "fringe"
		capacity[w[1]] = w[0]
		dad[w[1]] = s
	unvisited_queue = []
	for v in B.keys():
		if status[v]=="in-tree":
			for pair in B[v]:
				if status[pair[1]]=="fringe":
					unvisited_queue.append(pair)
	heapify_max(unvisited_queue)
	while(len(unvisited_queue)):
		uv = heappop(unvisited_queue)
		v = uv[1]
		status[v] = "in-tree"
		for w in B[v]:
			if status[w[1]]=="unseen":
				status[w[1]] = "fringe"
				dad[w[1]] = v
				capacity[w[1]] = minimum(capacity[v],w[0])
			elif(status[w[1]]=="fringe" and capacity[w[1]]<minimum(capacity[v],w[0])):
				dad[w[1]] = v
				capacity[w[1]] = minimum(capacity[v],w[0])
		#while(len(unvisited_queue)):
		#	heappop(unvisited_queue)
		unvisited_queue = []
		for v in B.keys():
			if status[v]=="in-tree":
				for pair in B[v]:
					if status[pair[1]]=="fringe":
						unvisited_queue.append(pair)
		heapify_max(unvisited_queue)
	#return dad
	i = t
	path = [t]
	while(dad[i]!=-1):
		path.append(dad[i])
		i = dad[i]
	path.reverse()
	print "Number of vertices traversed in maximum bandwidth path is : " + str(len(path))
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
	for i in vertex:
		if temp<capacity[i]:
			temp = capacity[i]
			v = i
	return v
	
#profile.run('randomGraph()')"""
randomGraph()
#s = A[random.randrange(0,5000,2)]
#t = A[random.randrange(1,5000,2)]
#print maxBandwidth(B,s,t)