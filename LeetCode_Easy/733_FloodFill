"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.
"""
import collections 

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        # rows are how many lists are inside the master list
        # columns are how many items inside each grid
        rows,columns = len(image),len(image[0])
        # mark nodes as visited in a set - if the coordinate is in the set, skip it
        visited = set()

        def bfs(node):
            queue = collections.deque() 
            # add node to visited and append to queue
            visited.add(node)
            queue.append(node)
            while queue:
                # pop the queue to get the row and col
                row, col = queue.popleft()
                # const directions
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                # for direction row and col
                for dr, dc in directions:
                    # if it is within range of rows and cols
                    # and is land and is not visited
                    if ((row+dr) in range(rows) and 
                        (col+dc) in range(columns) and
                        (image[row+dr][col+dc] == image[sr][sc]) and
                        (row+dr, col+dc) not in visited):
                        image[row+dr][col+dc] = color
                        # add to queue and add to visited
                        queue.append((row+dr,col+dc))
                        visited.add((row+dr,col+dc))

        bfs((sr,sc))
        image[sr][sc] = color


        return image

# Create an instance of the Solution class
solution_instance = Solution()

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
# Call the islandPerimeter method on the solution_instance
result = solution_instance.floodFill(image, sr, sc, color)
# Print the result
print(result)