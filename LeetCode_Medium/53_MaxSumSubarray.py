from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # let maxSum be the first element in the list
        maxSum = nums[0]
        # let curSum be 0
        curSum = 0

        # for each element in nums
        for n in nums:
            # if the curSum is less than 0
            if curSum < 0:
                # reset it to 0
                curSum = 0
            # otherwise, add it to the curSum
            curSum += n
            # let the max be the maximum between the current maximum and curSum
            maxSum = max(maxSum, curSum)
        return maxSum

# Create an instance of the Solution class
solution_instance = Solution()

# Define your input list of numbers
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Call the maxSubArray method on the solution_instance
result = solution_instance.maxSubArray(nums)

# Print the result
print(result)

# General algorithm:
# Initialize maxSum to be the first element in the list
# Initialize curSum to be 0
# Iterate the list one number at a time
# If the curSum is less than 0, reset it to 0
# Otherwise, add it to the curSum
# Let the max be the curSum compared to the stored max value
# Return the result
