from time import clock
import random
def undirectedRandomGraph(vertices,percentage):
	B = {}
	A = []
	maxEdge = (vertices*percentage)/100
	
	for i in range(vertices):
		A.append(i)
		B.update({i:[0,[]]})
		
	for v in range(vertices):
		for u in range(v+1,vertices):
			x = random.randrange(1,101)
			weight = random.randrange(1,1001)
			if(x<=percentage and B[v][0]<maxEdge and B[u][0]<maxEdge):
				B[v][1].append((weight,u))
				B[u][1].append((weight,v))
				B[v][0] += 1
				B[u][0] += 1
	
	s = A[random.randrange(len(A))]
	A.pop(A.index(s))
	t = A[random.randrange(len(A))]
	print "Starting point is: ",s
	print "Ending point is: ",t
	#return B,s,t
	"""print "Graph is : "
	for v in B:
		print v, ":",
		for pair in B[v][1]:
			print pair,
		print ""
	print "---------------------"""
	B = addEdges(B,s,t,vertices)
	return B,s,t

def addEdges(B,s,t,vertices):
	#print s
	start = s
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
	
#undirectedRandomGraph(10,30)

		
				
			
	