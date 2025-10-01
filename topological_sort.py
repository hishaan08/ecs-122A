#Topological Sort (Graph Algorithm)
def topological_sort(graph):
    n=len(graph)
    in_degree=[0]*n
    for u in range(n):
        for v in graph[u]:
            in_degree[v]+=1
    queue=[i for i in range(n) if in_degree[i]==0]
    result=[]
    while queue:
        u=queue.pop(0)
        result.append(u)
        for v in graph[u]:
            in_degree[v]-=1
            if in_degree[v]==0:
                queue.append(v)
    return result if len(result)==n else []
#Example: graph=[[1,2],[3],[3],[]]
#Complexity: O(V+E) time, O(V) space
