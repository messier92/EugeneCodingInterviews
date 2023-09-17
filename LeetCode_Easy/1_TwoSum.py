from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a dictionary to store previous values and their indexes
        prevdict = {}
        # iterate the list
        for i in range(len(nums)):
            # get the difference
            diff = target-nums[i]
            # if the difference is already in the dictionary
            if diff in prevdict:
                # return the indexes 
                return [prevdict[diff], i]
            # otherwise, add it into the dictionary
            prevdict[nums[i]] = i

# Define your input nums and target
nums = [2, 11, 7, 15]
target = 9

# Create an instance of the Solution class
solution_instance = Solution()

# Call the twoSum method on the instance and pass nums and target as arguments
result = solution_instance.twoSum(nums, target)

# Print the result
print("Indices of the two numbers that add up to the target:", result)
