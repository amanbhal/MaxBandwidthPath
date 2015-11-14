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
			weight = random.randrange(1,101)
			if(x<=percentage and B[v][0]<maxEdge and B[u][0]<maxEdge):
				B[v][1].append((weight,u))
				B[u][1].append((weight,v))
				B[v][0] += 1
				B[u][0] += 1
	
	s = A[random.randrange(len(A))]
	A.pop(A.index(s))
	t = A[random.randrange(len(A))]
	return B,s,t
	"""for v in B:
		print v, ":", B[v][0], "->",
		for pair in B[v][1]:
			print pair[1],
		print """
