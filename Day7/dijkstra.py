from heapq import heappush,heappop
def dijkstra(adj,src,dst):
    pq = []
    heappush(pq,(0,src))
    n = len(adj)
    result = [float("inf")]*n
    result[src] = 0
    while pq:
        dist,node = heappop(pq)
        
        for n,w in graph[node]:
            if (d:= dist+w) < result[n]:
                heappush(pq,(d,n))
                result[n] = d
    return result[dst]


n = int(input("Enter the number of nodes: "))
graph = []
for i in range(n):
    print("Enter the {i} node edges eg ( n, w ): ")
    while True:
        val = tuple(map,input("Enter (n, w): ").split())
        if not val:
            break
        
        
        
    
graph = [
    [(1,5),(2,10)],
    [(0,5),(3,10)],
    [(0,10),(3,6)],
    [(1,10),(2,6)]
]
print(dijkstra(graph,0,3))