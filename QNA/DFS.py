# Iterative solution
def depthFirstPrintIterative(graph, source):
    stack = [source]
    while len(stack) > 0:
        current = stack.pop();
        print(current)
        for neighbour in graph[current]:
            stack.append(neighbour)

# Recursive solution
def depthFirstPrintRecursion(graph, source):
    print(source)
    for neighbour in graph[source]:
        depthFirstPrintRecursion(graph, neighbour)
            
graph = {'a':['c','b'], 'b':['d'], 'c':['e'], 'd':['f'], 'e':[], 'f':[]}

print("Iterative:")
depthFirstPrintIterative(graph, 'a')
print("Recursive:")
depthFirstPrintRecursion(graph, 'a')
