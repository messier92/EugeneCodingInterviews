from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # instantiate islands
        islands = 0
        # iterate the row and cols of the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if it is part of an island, call BFS
                if grid[i][j] == '1':
                    # keep calling BFS as long as 1 is connected
                    self.callBFS(grid, i, j)
                    # finally, add to the total count of the islands
                    islands += 1
        return islands

    def callBFS(self, grid, i, j):
        # if it is not part of an island or beyond the boundaries 
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        # visited check - transform it into water as it has already been visited
        grid[i][j] = '0'
        # call BFS again to check if there are any other connections
        self.callBFS(grid, i+1, j)
        self.callBFS(grid, i-1, j)
        self.callBFS(grid, i, j+1)
        self.callBFS(grid, i, j-1)
        
# Define your grid
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

solution_instance = Solution()
number_of_islands = solution_instance.numIslands(grid)
print("Number of islands:", number_of_islands)
