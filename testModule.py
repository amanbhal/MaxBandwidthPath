import sys
import heapq
def maxBandwidth(B,s,t):
	status = ["unseen"]*6
	dad = [-1]*6
	capacity = [100]*6
	status[s] = "in-tree"
	for w in B[s]:
		status[w[1]] = "fringe"
		capacity[w[1]] = w[0]
		dad[w[1]] = s
	unvisited_queue = []
	for v in B.keys():
		if status[v]=="in-tree":
			for pair in B[v]:
				if status[pair[1]]=="fringe":
					unvisited_queue.append(pair)
	print unvisited_queue
	heapq._heapify_max(unvisited_queue)
	while(len(unvisited_queue)):
		uv = heapq.heappop(unvisited_queue)
		v = uv[1]
		status[v] = "in-tree"
		for w in B[v]:
			if status[w[1]]=="unseen":
				print str(w[1]) + " is unseen",
				status[w[1]] = "fringe"
				dad[w[1]] = v
				capacity[w[1]] = minimum(capacity[v],w[0])
				print " new capacity is : " + str(capacity[w[1]])
			elif(status[w[1]]=="fringe" and capacity[w[1]]<minimum(capacity[v],w[0])):
				print str(w[1]) + " is fringe",
				dad[w[1]] = v
				capacity[w[1]] = minimum(capacity[v],w[0])
				print " new capacity is : " + str(capacity[w[1]])
		#while(len(unvisited_queue)):
		#	heapq.heappop(unvisited_queue)
		unvisited_queue = []
		for v in B.keys():
			if status[v]=="in-tree":
				for pair in B[v]:
					if status[pair[1]]=="fringe":
						unvisited_queue.append(pair)
		print unvisited_queue
		heapq._heapify_max(unvisited_queue)
	#return dad
	i = t
	path = [t]
	while(dad[i]!=-1):
		path.append(dad[i])
		i = dad[i]
	path.reverse()
	print "Number of vertices traversed in maximum bandwidth path is : " + str(len(path))
	print path

def minimum(a,b):
	if(a<b):
		return a
	else:
		return b
	
B = {0:[(7,1),(4,2),(8,3)],
	1: [(7,0),(1,2)],
	2: [(4,0),(1,1),(3,4)],
	3: [(8,0),(2,4)],
	4: [(3,2),(2,3),(6,5)],
	5: [(6,4)]}

maxBandwidth(B,0,5)