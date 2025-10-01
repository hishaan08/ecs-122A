#Dijkstra's Algorithm (Shortest Path)
def dijkstra(graph,start):
    n=len(graph)
    dist=[float('inf')]*n
    dist[start]=0
    visited=set()
    for _ in range(n):
        u=min((i for i in range(n) if i not in visited),key=lambda x:dist[x])
        visited.add(u)
        for v,weight in graph[u]:
            if v not in visited and dist[u]+weight<dist[v]:
                dist[v]=dist[u]+weight
    return dist
#Example: graph=[[(1,4),(2,1)],[(2,2),(3,5)],[(3,1)],[]]
#Complexity: O(V^2) time, O(V) space
