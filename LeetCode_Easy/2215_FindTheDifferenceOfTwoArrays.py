from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert the input lists to sets for efficient membership testing
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the elements that are unique to each list
        unique_in_nums1 = list(set1 - set2)
        unique_in_nums2 = list(set2 - set1)
        
        # Create the result list containing the unique elements in each list
        result = [unique_in_nums1, unique_in_nums2]
        
        return result

# Example usage:
solution_instance = Solution()
nums1 = [1, 2, 3, 4, 5]
nums2 = [3, 4, 5, 6, 7]
result = solution_instance.findDifference(nums1, nums2)
print(result)  # Output will be [[1, 2], [6, 7]]
