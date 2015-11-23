import random
from randomGraph import *
import operator
from heapImplementation import *


def maxBandwidth_Kruskal_Fast(B,s,t,vertices):
	global dad
	global rank
	dad = [-1]*vertices
	rank = [0]*vertices
	edges = {}
	for i in range(1,1001):
		edges.update({i:[]})
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
			if (small,large) not in edges[pair[0]]:
				edges[pair[0]].append((small,large))
	delete = []
	for i in edges:
		if len(edges[i])==0:
			delete.append(i)
	for i in delete:
		del edges[i]
	edgeHeap = edges.keys()
	heapify_max(edgeHeap)
	T = []
	
	while(len(edgeHeap)):
		x = heappop(edgeHeap)
		while(len(edges[x])!=0):
			vertex = edges[x].pop()
			a = vertex[0]
			b = vertex[1]
			if a<b:
				v = a
				w = b
			else:
				v = b
				w = a
			s1 = FindModify(v)
			s2 = FindModify(w)
			if s1!=s2:
				T.append((v,w))
				Union(s1,s2)
		del edges[x]
	print "Kruskal Algo Over"
	#print "Maximum Spanning Tree is: ",T
	#makeGraph(B,T,s,t,vertices)
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
	delete = []
	for i in G:
		if len(G[i])==0:
			delete.append(i)
	for i in delete:
		del G[i]
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
	bandwidth = 1001
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

def FindModify(v):
	global dad
	w = v
	s = []
	while dad[w]!=-1:
		s.append(w)
		w = dad[w]
	while(len(s)!=0):
		v = s.pop()
		dad[v] = w
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

B,s,t = undirectedRandomGraph(3000,20)
start = clock()
maxBandwidth_Kruskal_Fast(B,s,t,3000)
stop = clock()
print "Time taken : ", (stop-start)
"""B = {0:[(7,1),(4,2),(8,3)],
	1: [(7,0),(1,2)],
	2: [(4,0),(1,1),(3,4)],
	3: [(8,0),(2,4)],
	4: [(3,2),(2,3),(6,5)],
	5: [(6,4)]}
maxBandwidth(B,0,5,6)"""