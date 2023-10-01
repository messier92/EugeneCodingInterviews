
def explore(graph, currentNode, visited):
    if currentNode in visited:
        return False
    visited.append(currentNode)
    for neighbor in graph[currentNode]:
        explore(graph, neighbor, visited)
    return True

def connectedComponentsCount(graph):
    visited = []
    count = 0
    for node in graph:
        if explore(graph, node, visited) == True:
            count+=1
    return count

nodes = {0:[8,1,5],1:[0],5:[0,8],8:[0,5],2:[3,4],3:[2,4],4:[3,2]}
print(connectedComponentsCount(nodes))
