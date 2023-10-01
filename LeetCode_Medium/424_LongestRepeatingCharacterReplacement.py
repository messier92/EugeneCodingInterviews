# Hint - Replace the characters that are less frequent
# Hint - use a Hashmap/Array and count the number of occurences of each character
# Hint - Sliding Window
# Take the length of the window and the count of the most frequent character - WindowLen-Count[B]

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Initialize a dictionary to count character frequencies.
        res = 0     # Initialize the result (maximum substring length).
        l = 0       # Initialize the left pointer.

        # Loop through the characters of the string from left to right (using 'r' as the right pointer).
        for r in range(len(s)):
            # Update the count dictionary with the current character 's[r]'.
            count[s[r]] = 1 + count.get(s[r], 0)
            # Check if the current substring length minus the maximum character count is greater than 'k'.
            while (r - l + 1) - max(count.values()) > k:
                # If the above condition is not met, increment the left pointer 'l'.
                count[s[l]] -= 1
                l += 1
            # Update the result with the maximum substring length so far.
            res = max(res, r - l + 1)
        return res  # Return the maximum substring length satisfying the conditions.

# Create an instance of the Solution class
solution_instance = Solution()

# Example usage:
input_string = "ABAB"
k = 2
result = solution_instance.characterReplacement(input_string, k)
print("Maximum substring length:", result)
