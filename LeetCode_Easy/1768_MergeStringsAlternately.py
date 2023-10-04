# Define the Solution class
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Init the list to store the result string 
        result = []
        # Get the minimum length
        min_len = min(len(word1), len(word2))
        
        # Merge characters alternately up to the length of the shorter word
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])

        # Append the remaining characters from the longer word
        if len(word1) > len(word2):
            result.append(word1[min_len:])
        elif len(word2) > len(word1):
            result.append(word2[min_len:])
        return "".join(result)

# Create an instance of the Solution class
solution_instance = Solution()

# Define two input words
word1 = "abc"
word2 = "12345"

# Call the mergeAlternately method on the solution_instance
result = solution_instance.mergeAlternately(word1, word2)

# Print the result
print(result)
