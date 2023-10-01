from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize an empty list to store frequencies
        freqList = []
        # Create a dictionary to count the occurrences of each element
        countDict = {}
        # Initialize a counter
        counter = 1

        # Iterate through the input list 'nums'
        for element in nums:
            if element not in countDict:
                # If the element is not in the dictionary, add it with a count of 1
                countDict[element] = counter
            else:
                # If the element is already in the dictionary, increment its count
                countDict[element] = countDict[element] + 1

        # Sort the dictionary by values in descending order
        sorted_countDict = dict(sorted(countDict.items(), key=lambda item: item[1], reverse=True))

        # Extract keys (elements) from the sorted dictionary
        for key, value in sorted_countDict.items():
            freqList.append(key)

        # Take the first 'k' elements from the sorted list (top K frequent elements)
        freqList = freqList[:k]

        return freqList

# Create an instance of the Solution class
solution_instance = Solution()

# Example usage:
input_nums = [1, 1, 1, 2, 2, 3]
k = 2
result = solution_instance.topKFrequent(input_nums, k)
print("Top", k, "frequent elements:", result)
