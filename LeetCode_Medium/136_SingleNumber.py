class Solution:
    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]

        sorted_nums = sorted(nums)
        for index, value in enumerate(sorted_nums):
            # If it is the first element in the list
            if index == 0 and value != sorted_nums[index+1]:
                return value
            # Check if the current element is neither the first nor the last
            elif 0 < index < len(sorted_nums) - 1:
                if (value != sorted_nums[index-1] and value != sorted_nums[index+1]):
                    return value
            # Check if the current element is the last element
            elif index == len(sorted_nums) - 1 and value != sorted_nums[index-1]:
                return value

# Example usage:
solution_instance = Solution()
nums = [4, 1, 2, 1, 2]
result = solution_instance.singleNumber(nums)
print(result)  # Output will be 4
