def hasPathBFSIterative(graph, src, dst):
    queue = [src]

    while len(queue) > 0:
        current = queue.pop(0)
        if current == dst:
            return True

        for neighbor in graph[current]:
            queue.append(neighbor)

    return False

def hasPathDFSRecursive(graph, src, dst):
    if src == dst:
        return True
    for neighbor in graph[src]:
        if hasPathDFSRecursive(graph, neighbor, dst) == True:
            return True
    return False

graph = {'f':['g','i'], 'g':['h'], 'h':[], 'i':['g','k'], 'j':['i'],'k':[]}
print(hasPathDFSRecursive(graph, 'f','j'))
print(hasPathBFSIterative(graph, 'f','k'))
