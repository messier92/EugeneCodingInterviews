# Rotate Image clockwise in place
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # init l and r pointers
        l, r = 0, len(matrix) - 1
        # while left is less than right pointer
        while l<r:
            # for each column
            for i in range(r-l):
                # init top and bottom pointers
                top, bottom = l, r
                
                # store the top left element
                topLeft=matrix[top][l+i]
                # move element bottom left to top left
                matrix[top][l+i]=matrix[bottom-i][l]
                # move element bottom right to bottom left
                matrix[bottom-i][l]=matrix[bottom][r-i]
                # move element top right to bottom right
                matrix[bottom][r-i]=matrix[top+i][r]
                
                # move element top left to top right
                matrix[top+i][r]=topLeft
            # decrement right pointer
            r-=1
            # increment left pointer
            l+=1

solution = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
solution.rotate(matrix)
for row in matrix:
    print(row)
