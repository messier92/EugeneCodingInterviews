"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr_str = ""
        curr_num = 0

        for char in s:
            if char.isdigit():
               # Build the multiplier (handles multi-digit like '12')
               curr_num = curr_num * 10 + int(char)
            elif char == '[':
               # We are going deeper: save what we have so far
               stack.append((curr_str, curr_num))
               curr_str = ""
               curr_num = 0
            elif char == ']':
               # We are coming out: pop the last state
               prev_str, num = stack.pop()
               # Multiply the inner part and attach to the outer part
               curr_str = prev_str + (num * curr_str)
            else:
               # Just a letter, add to the current segment
               curr_str += char
               
        return curr_str

# Create an instance of the Solution class
solution_instance = Solution()

# Example usage:
input_string = "3[a2[c]]"
result = solution_instance.decodeString(input_string)
print("Decoded string:", result)
