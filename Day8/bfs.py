# How can we traverse a graph using breadth-first search?
from collections import deque

def bfs(src, adj, visited):
    q = deque([src])
    visited[src] = True
    
    while q:
        node = q.popleft()
        print(node, end=" ")
        
        for ngbr in adj[node]:
            if not visited[ngbr]:
                visited[ngbr] = True
                q.append(ngbr)
                
n = int(input("Enter the number of nodes: "))
graph = []
for i in range(n):
    graph.append(list(map(int,input(f"Enter the neighbor nodes of {i} node: eg: 1 2 3 : ").split())))
bfs(graph,0)

"""
1. Add the source node to a queue and mark it as visited.
2. Remove the oldest node from the queue and print it.
3. Add each unvisited neighbor to the queue and mark it immediately.
4. Continue until the queue is empty.
"""
    
    