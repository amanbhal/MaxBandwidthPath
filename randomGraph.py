from time import clock
import random
def randomGraph(vertices,links):
	B = {}
	A = []
	conditionForAll = []
	for i in range(vertices):
		A.append(i)
		B.update({i:[]})
		conditionForAll.append(True)
	condition = True
	while(condition==True):
		u = random.randrange(vertices)
		v = random.randrange(vertices)
		weight = random.randrange(1,101)
		if u==v or len(B[v])==links or len(B[u])==links:
			continue
		for v in B.keys():
			if(len(B[v])>=links):
				conditionForAll[v] = False
		result = False
		for v in B.keys():
			result = result or conditionForAll[v]
		if(result==False):
			condition = False
			continue
		else:
			condition = True
		B[v].append((weight,u))
		B[u].append((weight,v))
	for i in range(vertices):
		A.append(i)
	s = A[random.randrange(0,vertices,2)]
	t = A[random.randrange(1,vertices,2)]
	for v in B:
		print v, ":",
		for pair in B[v]:
			print pair[1],
		print ""
randomGraph(5,2)