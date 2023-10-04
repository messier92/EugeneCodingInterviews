from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                # If we've reached the end of the list, add the current permutation to the result.
                result.append(nums[:])
            for i in range(start, len(nums)):
                # Swap the current element with the element at index 'start'.
                nums[start], nums[i] = nums[i], nums[start]
                # Recursively generate permutations for the rest of the list.
                backtrack(start + 1)
                # Undo the swap to backtrack and explore other possibilities.
                nums[start], nums[i] = nums[i], nums[start]
        result = []  # Initialize a list to store the permutations.
        backtrack(0)  # Start generating permutations from index 0.
        return result

# Create an instance of the Solution class
solution_instance = Solution()

# Example usage:
nums = [1, 2, 3]
permutations = solution_instance.permute(nums)
print(permutations)
