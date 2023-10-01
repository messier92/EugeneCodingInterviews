# boilerplate code to build graph
def buildGraph(edges):
    graph = {}
    for edge in edges:
        [a,b] = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b);
        graph[b].append(a);
    return graph

def hasPath(graph, src, dst, visited):
    # check if src is already visited
    if src in visited:
        return False
    # append the current src to visited
    visited.append(src)
    
    if (src == dst):
        return True
    for neighbor in graph[src]:
        if (hasPath(graph, neighbor, dst, visited)) == True:
            return True

    return False
    
def undirectedPath(edges, nodeA, nodeB):
    visited = []
    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB, visited)
    
edges = [['i','j'],['k','i'],['m','k'],['k','l'],['o','n']];
print(undirectedPath(edges, 'j', 'm'))
