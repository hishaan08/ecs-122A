#Breadth-First Search (Graph Algorithm)
def bfs(graph,start):
    visited=set()
    queue=[start]
    visited.add(start)
    result=[]
    while queue:
        node=queue.pop(0)
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result
#Example: graph={0:[1,2],1:[0,3],2:[0,3],3:[1,2]}
#Complexity: O(V+E) time, O(V) space
