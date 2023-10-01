### Maze Problem DP ###

def grid_paths(n,m):
    memo = {}
    # If it is on the extreme right, then the only path is down
    for i in range(1, n+1):
        memo[(i,1)] = 1
    # If it is on the extreme bottom, then the only path is right
    for j in range(1, m+1):
        memo[(1,j)] = 1

    # Otherwise, if it is not in the bottom or right boundaries of the grid,
    # iterate the row and col by summing the bottom and right possibilities
    for i in range(2, n+1):
        for j in range(2, m+1):
            memo[(i,j)] = memo[(i-1,j)]+memo[(i,j-1)]
    return memo[(n,m)]

print(grid_paths(170,60))
