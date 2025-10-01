#Prim's Algorithm (Minimum Spanning Tree)
def prims_mst(graph):
    n=len(graph)
    mst=[]
    key=[float('inf')]*n
    parent=[-1]*n
    mst_set=[False]*n
    key[0]=0
    for _ in range(n):
        u=min((i for i in range(n) if not mst_set[i]),key=lambda x:key[x])
        mst_set[u]=True
        if parent[u]!=-1:
            mst.append((parent[u],u,key[u]))
        for v,weight in graph[u]:
            if not mst_set[v] and weight<key[v]:
                key[v]=weight
                parent[v]=u
    return mst
#Example: graph=[[(1,2),(2,3)],[(0,2),(2,1)],[(0,3),(1,1)]]
#Complexity: O(V^2) time, O(V) space
