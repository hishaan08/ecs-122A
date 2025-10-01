#Bellman-Ford Algorithm (Shortest Path with Negative Weights)
def bellman_ford(graph,start):
    n=len(graph)
    dist=[float('inf')]*n
    dist[start]=0
    for _ in range(n-1):
        for u in range(n):
            for v,weight in graph[u]:
                if dist[u]+weight<dist[v]:
                    dist[v]=dist[u]+weight
    for u in range(n):
        for v,weight in graph[u]:
            if dist[u]+weight<dist[v]:
                return None
    return dist
#Example: graph=[[(1,4),(2,1)],[(2,2),(3,5)],[(3,1)],[]]
#Complexity: O(VE) time, O(V) space
