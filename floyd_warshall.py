#Floyd-Warshall Algorithm (All-Pairs Shortest Path)
def floyd_warshall(graph):
    n=len(graph)
    dist=[[float('inf')]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                dist[i][j]=0
            elif graph[i][j]!=0:
                dist[i][j]=graph[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k]+dist[k][j]<dist[i][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
    return dist
#Example: graph=[[0,5,float('inf'),10],[float('inf'),0,3,float('inf')],[float('inf'),float('inf'),0,1],[float('inf'),float('inf'),float('inf'),0]]
#Complexity: O(V^3) time, O(V^2) space
