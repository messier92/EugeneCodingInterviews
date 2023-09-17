from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize the max product as the first element in the list
        maxProduct = nums[0]
        # Initialize variables for current minimum and maximum products as 1
        curMin, curMax = 1, 1

        # Iterate through each element in nums
        for n in nums:
            # If the current element is 0, reset curMin and curMax to 1
            if n == 0:
                curMin, curMax = 1, 1
            # Calculate the temporary maximum product ending at the current element
            tmp = curMax * n
            # Update curMax as the maximum among tmp, curMin * n, and n
            curMax = max(tmp, curMin * n, n)
            # Update curMin as the minimum among tmp, curMin * n, and n
            curMin = min(tmp, curMin * n, n)
            # Update maxProduct as the maximum between maxProduct and curMax
            maxProduct = max(maxProduct, curMax)
        
        # Return the maximum product found
        return maxProduct

# Create an instance of the Solution class
solution_instance = Solution()

# Define your input list of numbers
nums = [2, 3, -2, 4]

# Call the maxProduct method on the solution_instance
result = solution_instance.maxProduct(nums)

# Print the result
print(result)




