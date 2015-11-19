from time import clock
import random
def undirectedSparseRandomGraph(vertices):
	B = {}
	A = []
	maxEdge = 5
	
	for i in range(vertices):
		A.append(i)
		B.update({i:[0,[]]})
		
	for u in range(vertices):
		arrayList = []
		for v in range(vertices):
			if(B[v][0]<maxEdge and v!=u):
				arrayList.append(v)
		left = maxEdge - B[u][0]
		n = len(arrayList)
		k = 0
		while(k<n and left>0):
			r = random.randrange(n-k)
			temp = arrayList[n-k-1]
			arrayList[n-k-1] = arrayList[r]
			arrayList[r] = temp
			w = arrayList[n-k-1]
			weight = random.randrange(1,1001)
			B[u][1].append((weight,w))
			B[w][1].append((weight,u))
			B[w][0] += 1
			B[u][0] += 1
			k += 1
			left -= 1
			#print u,w
			
		
	s = A[random.randrange(len(A))]
	A.pop(A.index(s))
	t = A[random.randrange(len(A))]
	#print "Starting point is: ",s
	#print "Ending point is: ",t
	#return B,s,t"""
	#print "Graph is : "
	"""for v in B:
		print v, ":", B[v][0]
	print "---------------------"""
	"""print "Graph is : "
	for v in B:
		print v, ":",
		for pair in B[v][1]:
			print pair,
		print ""
	print "---------------------"""
	for v in B.keys():
		if(B[v][0]!=5):
			#print "Fault",v
			#B.clear()
			undirectedSparseRandomGraph(5000)
			B = addEdges(B,s,t,vertices)
			return B,s,t
		for pair in B[v][1]:
			count = 0
			for x in B[v][1]:
				if x[1]==pair[1]:
					count+=1
			if count>1:
				#print "Fault",v,pair[1]
				#B.clear()
				undirectedSparseRandomGraph(5000)
				B = addEdges(B,s,t,vertices)
				return B,s,t
	B = addEdges(B,s,t,vertices)
	return B,s,t
#B,s,t = undirectedSparseRandomGraph(100)
#print len(B),s,t

def addEdges(B,s,t,vertices):
	start = s
	#print s
	for i in range(vertices):
		weight = random.randrange(1,1001)
		if(i!=start and i!=t):
			#print i
			B[i][1].append((weight,s))
			B[s][1].append((weight,i))
			B[i][0] += 1
			B[s][0] += 1
			s = i
	#print t
	weight = random.randrange(1,1001)
	B[s][1].append((weight,t))
	B[t][1].append((weight,s))
	B[s][0] += 1
	B[t][0] += 1
	return B

#undirectedSparseRandomGraph(10)
