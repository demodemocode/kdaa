import queue

num_vertices = int(input("Enter number vertices: "))
num_edges = int(input("Enter number of edges: "))

def netdelay(edges,vertices,start):
	graph = [[] for i in range(vertices)]
	for u,v,w in edges:
		graph[u].append((v,w))
	dist = [float('inf')] * vertices
	dist[start] = 0
	pq = queue.PriorityQueue()
	pq.put((0,start))
	
	while not pq.empty():
		distance, u = pq.get()
		if distance > dist[u]:
			continue
		
		for v,weight in graph[u]:
			if dist[u] + weight < dist[v]:
				dist[v] = dist[u] + weight
				pq.put((dist[v],v))
	
	for i in range(vertices):
		if dist[i] == float('inf'):
			return -1
	
	return max(dist)
			 
	

print("Enter source destintion weight space seprated ")
edges = [tuple(map(int,input().split())) for i in range(num_edges)]

start = int(input("Eneter start: "))

time = netdelay(edges,num_vertices, start)

print (time)
