# Import List from the typing module
from typing import List

# Define the Solution class (assuming you've already defined it in your code)
class Solution:
    def find132pattern(self, nums):
        n = len(nums) # get length of nums
        if n < 3: # if length of nums is less than 3, return false
            return False
        stack = []  # init the stack
        max2 = float('-inf')  # Maximum "2" element found so far
        # iterate the length of the list from the end
        for i in range(n - 1, -1, -1):
            # if a valid "132" pattern is found
            if nums[i] < max2:
                return True  # Found a valid "132" pattern if nums[i] is less than max2
            # while nums[i] is greater than the first element of the stack
            while stack and nums[i] > stack[-1]:
                # Update max2 by popping the stack                
                max2 = stack.pop() 
            # Push the current element onto the stack
            stack.append(nums[i])
        return False

# Create an instance of the Solution class
solution = Solution()
# Example usage with an input list of numbers
nums = [3, 1, 4, 2]
result = solution.find132pattern(nums)
# Print the result
print(result)  # This will print True for the given input
