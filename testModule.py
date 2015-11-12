import sys
import time
def maxBandwidth(B,s,t):
	global dad
	global rank
	dad = [-1]*6
	rank = [0]*6
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
		#print "Edge is : " + str(v) + "," + str(w),
		s1 = Find(v)
		s2 = Find(w)
		if s1!=s2:
			T.append((v,w))
			Union(s1,s2)
	print t,
	w = t
	path = [-1]*6
	for pair in T:
		path[pair[1]] = pair[0]
	while(path[w]!=s):
		print path[w],
		w = path[w]
	print s
	
			
def MakeSet(v):
	global dad
	global rank
	dad[v] = 0
	rank[v] = 0
	
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
	
	
B = {0:[(7,1),(4,2),(8,3)],
	1: [(7,0),(1,2)],
	2: [(4,0),(1,1),(3,4)],
	3: [(8,0),(2,4)],
	4: [(3,2),(2,3),(6,5)],
	5: [(6,4)]}
	
start = time.time()	
maxBandwidth(B,0,5)
stop = time.time() - start
print stop