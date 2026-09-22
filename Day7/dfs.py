
def dfs(adj,src):
    stack = [src]
    n = len(adj)
    visited = [False]*n
    while stack:
        node = stack.pop()
        if not visited[node]:
            print(node,end=" ")
        visited[node] = True
        for ngbr in adj[node]:
            if not visited[ngbr]:
                stack.append(ngbr)

# graph=[
#     [1,2,3],
#     [0,4],
#     [0,5],
#     [0,6],
#     [1,8],
#     [2,7],
#     [3,7],
#     [5,6,8],
#     [4,7]
# ]
n = int(input("Enter the number of nodes: "))
graph = []
for i in range(n):
    graph.append(list(map(int,input(f"Enter the neighbor nodes of {i} node: eg: 1 2 3 : ").split())))
dfs(graph,0)
    
    