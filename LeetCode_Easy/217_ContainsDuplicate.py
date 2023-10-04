from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Get the length of the nums list
        numsLength = len(nums)
        # Create a set from the nums list, which automatically removes duplicates
        numsSet = set(nums)
        # Check if the length of the set is equal to the length of the original list
        # If they are equal, it means there are no duplicates, so return False
        if numsLength == len(numsSet):
            return False
        else:
            # If the lengths are not equal, it means there are duplicates, so return True
            return True

# Create an instance of the Solution class
solution_instance = Solution()
# Define your input list of numbers
numbers = [1, 2, 3, 4, 5, 5]
# Call the containsDuplicate method on the solution_instance
result = solution_instance.containsDuplicate(numbers)
# Print the result (True if there are duplicates, False if there are no duplicates)
print(result)
