from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the length of the input list is 0, return an empty string
        if len(strs) == 0:
            return ""
        # Let the base case be the first string in the list
        base = strs[0]
        # Iterate through each character position in the first string
        for i in range(len(base)):
            # Iterate through each remaining word in the list
            for word in strs[1:]:
                # If the current position exceeds the length of the word
                # or if the character in the base string doesn't match the character in the word
                if i == len(word) or base[i] != word[i]:
                    # Return the common prefix found so far (up to the current position)
                    return base[0:i]
        # If no mismatch was found, return the entire base string as the common prefix
        return base

# Example usage:
solution_instance = Solution()
input_strings = ["flight", "flow", "flower"]
result = solution_instance.longestCommonPrefix(input_strings)
print(result)  # Output will be "fl"
