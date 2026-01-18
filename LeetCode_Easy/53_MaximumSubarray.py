"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best_sum = float('-inf')
        curr_sum = 0
        best_start = 0
        best_end = 0
        current_start = 0
        
        for i, x in enumerate(nums):
            # Equivalent to: curr_sum = max(x, x + curr_sum)
            if x > x + curr_sum:
                curr_sum = x
                current_start = i  # Reset start index if we start a new subarray
            else:
                curr_sum = x + curr_sum

            # Equivalent to: best_sum = max(best_sum, curr_sum)
            if curr_sum > best_sum:
                best_sum = curr_sum
                best_start = current_start
                best_end = i

        return best_sum, best_start, best_end

solution_instance = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]

max_sum, start, end = solution_instance.maxSubArray(nums)

print("Maximum Sum:", max_sum)
print("Indices:", start, "to", end)
print("Subarray:", nums[start:end+1])