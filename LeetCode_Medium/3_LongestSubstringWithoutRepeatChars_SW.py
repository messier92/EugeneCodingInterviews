class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {} # Create a dictionary to store the last seen index of each character.
        max_length = 0 # Set max length to 0
        start = 0  # Start of the sliding window

        # for each character in the string
        for end in range(len(s)):
            if s[end] in char_index:
                # If the character is already in the dictionary, update the start pointer
                # to the next position after the last occurrence of the character.
                start = max(start, char_index[s[end]] + 1)

            # Update the last seen index of the character.
            char_index[s[end]] = end

            # Calculate the length of the current substring.
            current_length = end - start + 1
            # Update the maximum length if necessary.
            max_length = max(max_length, current_length)
        return max_length

# Create an instance of the Solution class
solution_instance = Solution()

# Example usage:
input_string = "abcabcbb"
result = solution_instance.lengthOfLongestSubstring(input_string)
print("Length of the longest substring without repeating characters:", result)
