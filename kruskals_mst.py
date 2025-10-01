#Kruskal's Algorithm (Minimum Spanning Tree)
def kruskals_mst(edges,n):
    edges.sort(key=lambda x:x[2])
    parent=list(range(n))
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(x,y):
        px,py=find(x),find(y)
        if px!=py:
            parent[px]=py
            return True
        return False
    mst=[]
    for u,v,weight in edges:
        if union(u,v):
            mst.append((u,v,weight))
    return mst
#Example: edges=[(0,1,2),(0,2,3),(1,2,1)], n=3
#Complexity: O(E log E) time, O(V) space
