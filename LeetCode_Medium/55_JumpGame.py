from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1  # The goal is to reach the last index of the array
        
        # Start at the end and move towards the first index with a decrement of 1
        for i in range(len(nums) - 1, -1, -1):
            # If we can reach the current index 'i' from a previous index, update the 'goal' to 'i'
            if i + nums[i] >= goal:
                goal = i
        
        # If 'goal' eventually becomes 0, it means we can reach the last index from the first index
        if goal == 0:
            return True
        else:
            return False

# Now, create an instance of the Solution class
solution_instance = Solution()

# Define the input list
nums = [2, 3, 1, 1, 4]

# Call the canJump method on the instance and print the result
result = solution_instance.canJump(nums)
print(result)  # This will print True if it's possible to jump to the last index, otherwise False
