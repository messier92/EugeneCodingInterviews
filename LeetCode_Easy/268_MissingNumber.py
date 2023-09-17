from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # get the length of the list
        lengthOfNums = len(nums)
        lengthOfNumsList = []
        # have to make n = 1 because 0 doesn't count and take up a space
        n = 1
        # for example, 
        # if len(nums) = 3, then we want the expected sum to be 1+2+3 = 6
        # if len(nums) = 5, we want the expected sum to be 1+2+3+4+5 = 15
        # add in each element into the list
        for i in range(lengthOfNums):
            lengthOfNumsList.append(n)
            n+=1
        # Calculate the expected sum 
        expected_sum = sum(lengthOfNumsList)
        # Calculate the actual sum of the elements in the input list
        actual_sum = sum(nums)
        # The missing number is the difference between the expected sum and the actual sum
        return expected_sum - actual_sum

# Create an instance of the Solution class
solution_instance = Solution()
# Define your input list
nums = [0, 2, 3]
# Call the missingNumber method on the solution_instance
result = solution_instance.missingNumber(nums)
# Print the result
print(result)






