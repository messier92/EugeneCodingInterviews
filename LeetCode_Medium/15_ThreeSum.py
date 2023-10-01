class Solution:
    def threeSum(self, nums):
        res = []                        # Initialize a list to store the unique triplets
        sorted_nums = sorted(nums)      # Sort the input list to simplify the process

        for i, v in enumerate(sorted_nums):
            if i > 0 and v == sorted_nums[i - 1]:
                continue  # Skip duplicates to avoid duplicate triplets

            l, r = i + 1, len(sorted_nums) - 1  # Initialize left and right pointers

            while l < r:
                threeSum = v + sorted_nums[l] + sorted_nums[r]

                if threeSum > 0:  # If the sum is too large, move the right pointer to the left
                    r -= 1
                elif threeSum < 0:  # If the sum is too small, move the left pointer to the right
                    l += 1
                else:
                    res.append([v, sorted_nums[l], sorted_nums[r]])  # Triplet found, add it to the result
                    l += 1
                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l += 1  # Skip duplicates in the left pointer

        return res  # Return the list of unique triplets that sum to zero

# Example usage:
solution_instance = Solution()
nums = [-1, 0, 1, 2, -1, -4]
result = solution_instance.threeSum(nums)
print(result)  # Output will be [[-1, -1, 2], [-1, 0, 1]]
