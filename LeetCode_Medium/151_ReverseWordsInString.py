# Define the Solution class
class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string by whitespaces into a list
        s = s.split()
        # Reverse the list
        s = s[::-1]
        # Join each element in the list with a whitespace between them
        return ' '.join(s)

# Create an instance of the Solution class
solution_instance = Solution()

# Define the input string
input_string = "Hello World"

# Call the reverseWords method on the solution_instance
result = solution_instance.reverseWords(input_string)

# Print the result
print(result)  # Output will be "World Hello"
