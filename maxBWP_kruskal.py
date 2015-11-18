import random
from randomGraph import *
import operator

def directedRandomGraph(vertices,links):
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
	"""for v in B:
		print v, ":",
		for pair in B[v]:
			print pair,
		print """
	print "Starting Point is : " + str(s)
	print "Ending Point is : " + str(t)
	maxBandwidth(B,s,t,vertices)

def maxBandwidth_Kruskal(B,s,t,vertices):
	global dad
	global rank
	dad = [-1]*vertices
	rank = [0]*vertices
	edges = {}
	for v in B.keys():
		for pair in B[v][1]:
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
	#edgeWeight = edges.values()
	#edgeWeight.sort(key=operator.itemgetter(0))
	#edgeWeight.reverse()
	#print edgeWeight
	T = []
	#for v in B.keys():
	#	MakeSet(v)
	#for weight in edgeWeight:
	#	v = -1
	#	w = -1
	for vertex in sorted(edges,key=edges.__getitem__,reverse=True):
		#if edges[vertex][0]==weight[0] and edges[vertex][1]==False:
		#print vertex
		v = vertex[0]
		w = vertex[1]
			#edges[vertex] = (weight[0],True)
		s1 = Find(v)
		s2 = Find(w)
		if s1!=s2:
			T.append((v,w))
			Union(s1,s2)
	#print "Maximum Spanning Tree is: ",T
	makeGraph(B,T,s,t,vertices)
	"""if t>s:
		print t,
		w = t
	else:
		print s,
		w = s
	path = [-1]*vertices
	for pair in T:
		path[pair[1]] = pair[0]
	while(path[w]!=-1):
		print path[w],
		w = path[w]
	if t>s:
		print s
	else:
		print t"""
		
def makeGraph(B,T,s,t,vertices):
	G = {}
	for i in range(vertices):
		G.update({i:[]})
	for pair in T:
		G[pair[0]].append(pair[1])
		G[pair[1]].append(pair[0])
	global color
	global path
	path = [-1]*vertices
	color = ["white"]*vertices
	DFSpath(G,s,t)
	#print "Path is : ",
	#print path
	answer = []
	w = t
	while(path[w]!=-1):
		answer.append(w)
		w = path[w]
	answer.append(s)
	bandwidth = 1000
	for i in range(len(answer)-1):
		v = answer[i]
		u = answer[i+1]
		for x in B.keys():
			if x==v:
				for y in B[v][1]:
					if y[1]==u:
						if bandwidth>y[0]:
							bandwidth = y[0]
	print "Number of vertices traversed in maximum bandwidth path is : ", len(answer), "with bandwidth: ", bandwidth
	answer.reverse()
	print answer
	
def DFSpath(G,s,t):
	global path
	color[s] = "grey"
	for i in G[s]:
		if color[i]=="white":
			path[i] = s
			DFSpath(G,i,t)
	color[s] = "black"
	
	
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

#B,s,t = undirectedRandomGraph(50,10)
#print "Starting Point : ",s
#print "Ending Point : ",t
#start = clock()
#maxBandwidth(B,s,t,50)
#stop = clock()
#print "Time taken : ", (stop-start)
"""B = {0:[(7,1),(4,2),(8,3)],
	1: [(7,0),(1,2)],
	2: [(4,0),(1,1),(3,4)],
	3: [(8,0),(2,4)],
	4: [(3,2),(2,3),(6,5)],
	5: [(6,4)]}
maxBandwidth(B,0,5,6)"""