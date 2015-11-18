from time import clock
import random
def undirectedSparseRandomGraph(vertices):
	B = {}
	A = []
	maxEdge = 6
	
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
			weight = random.randrange(1,101)
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
	"""print "Starting point is: ",s
	print "Ending point is: ",t
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
		if(B[v][0]!=6):
			print "Fault",v
		for pair in B[v][1]:
			count = 0
			for x in B[v][1]:
				if x[1]==pair[1]:
					count+=1
			if count>1:
				print "Fault",v,pair[1]
undirectedSparseRandomGraph(5000)