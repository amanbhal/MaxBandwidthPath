def maxBandwidth(B,s,t):
	status = ["unseen"]*6
	dad = [-1]*6
	capacity = [0]*6
	status[s] = "in-tree"
	for w in B[s]:
		status[w[1]] = "fringe"
		capacity[w[1]] = w[0]
		dad[w[1]] = s
	while("fringe" in status):
		v = largestFringe(status,capacity)
		status[v] = "in-tree"
		for w in B[v]:
			if status[w[1]]=="unseen":
				status[w[1]] = "fringe"
				dad[w[1]] = v
				capacity[w[1]] = minimum(capacity[v],w[0])
			elif(status[w[1]]=="fringe" and capacity[w[1]]<minimum(capacity[v],w[0])):
				dad[w[1]] = v
				capacity[w[1]] = minimum(capacity[v],w[0])
	#print dad
	i = t
	path = [t]
	while(dad[i]!=-1):
		path.append(dad[i])
		i = dad[i]
	path.reverse()
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

B = {0:[(7,1),(4,2),(8,3)],
	1: [(7,0),(1,2)],
	2: [(4,0),(1,1)],
	3: [(8,0)],
	4: [(6,5)],
	5: [(6,4)]}

maxBandwidth(B,1,5)