"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""
import collections 
# Define the Solution class
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # initialize variables and constants
        rows = len(grid)
        columns = len(grid[0])
        rollingPerimeter = 0

        # always add 4 when you come to a node, subtracted by the number of other nodes it is connected to
        def findConnectedNodes(node):
            numberOfNodes = 0
            queue = collections.deque()
            queue.append(node)
            while queue:
                # pop the queue to get the row and col
                row, col = queue.popleft()
                # const directions
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    if ((row+dr) in range(rows) and 
                        (col+dc) in range(columns) and
                        grid[row+dr][col+dc] == 1):
                        numberOfNodes += 1
            return numberOfNodes
            
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    constPerimeter = 4
                    numOfConnectedNodes = findConnectedNodes((r,c))
                    nodePerimeter = constPerimeter - numOfConnectedNodes
                    rollingPerimeter+=nodePerimeter
                else:
                    continue
        return rollingPerimeter

# Create an instance of the Solution class
solution_instance = Solution()

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

# Call the islandPerimeter method on the solution_instance
result = solution_instance.islandPerimeter(grid)

# Print the result
print(result)


