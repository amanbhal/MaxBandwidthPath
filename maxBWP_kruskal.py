import profile
import random
import timeit
import time
from datetime import datetime

def randomGraph(vertices,links):
	#start = timeit.default_timer()
	#start = datetime.now().microsecond
	##start = time.time()
	B = {}
	A = []
	for i in range(vertices):
		A.append(i)
		B.update({i:[]})
		
	for i in range(vertices):
		start = random.randrange(0,vertices-links)
		A.pop(A.index(i))
		random.shuffle(A)
		for j in A[start:start+links]:
			B[i].append((random.randrange(1,101),j))
		A.append(i)
	#stop = timeit.default_timer()
	#stop = datetime.now().microsecond
	##print (time.time() - start)
	s = A[random.randrange(0,vertices,2)]
	t = A[random.randrange(1,vertices,2)]
	print "Starting Point is : " + str(s)
	print "Ending Point is : " + str(t)
	maxBandwidth(B,s,t,vertices)

def maxBandwidth(B,s,t,vertices):
	global dad
	global rank
	dad = [-1]*vertices
	rank = [0]*vertices
	edges = {}
	for v in B.keys():
		for pair in B[v]:
			small = -1
			large = -1
			if v<pair[1]:
				small = v
				large = pair[1]
			else:
				small = pair[1]
				large = v
			if (small,large) not in edges.keys():
				edges.update({(small,large):(pair[0],False)})
	edgeWeight = edges.values()
	edgeWeight.sort()
	edgeWeight.reverse()
	T = []
	#for v in B.keys():
	#	MakeSet(v)
	for weight in edgeWeight:
		v = -1
		w = -1
		for vertex, weightVisited in edges.items():
			if weightVisited[0]==weight[0] and weightVisited[1]==False:
				v = vertex[0]
				w = vertex[1]
				weightVisited = True
		s1 = Find(v)
		s2 = Find(w)
		if s1!=s2:
			T.append((v,w))
			Union(s1,s2)
	print t,
	w = t
	path = [-1]*vertices
	for pair in T:
		path[pair[1]] = pair[0]
	while(path[w]!=s):
		print path[w],
		w = path[w]
	print s
	
def MakeSet(v):
	global dad
	global rank
	dad[v] = -1
	rank[v] = -1
	
def Find(v):
	global dad
	w = v
	while dad[w]!=-1:
		w = dad[w]
	return w
	
def Union(s1,s2):
	global dad
	global rank
	if(rank[s1]>rank[s2]):
		dad[s2] = s1
	elif(rank[s2]>rank[s1]):
		dad[s1] = s2
	else:
		dad[s2] = s1
		rank[s1] += 1
randomGraph(5000,1000)