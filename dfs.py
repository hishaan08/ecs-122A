#Depth-First Search (Graph Algorithm)
def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)
    result=[start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph,neighbor,visited))
    return result
#Example: graph={0:[1,2],1:[0,3],2:[0,3],3:[1,2]}
#Complexity: O(V+E) time, O(V) space
