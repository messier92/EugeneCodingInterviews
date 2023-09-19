class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Define a set containing vowels
        vowelSet = {'a', 'e', 'i', 'o', 'u'}
        
        # Initialize pointers and variables
        pointerA = 0   # Start of the current substring
        count = 0      # Count of vowels in the current substring
        result = 0     # Maximum count of vowels seen so far
        
        # Iterate through the characters of the input string
        for pointerB in range(len(s)):
            # Check if the character at pointerB is a vowel and increment count if it is
            count += 1 if s[pointerB] in vowelSet else 0
            
            # Check if the length of the current substring exceeds k
            if pointerB - pointerA + 1 > k:
                # If it does, check if the character at pointerA (start of substring) is a vowel
                # If it is, decrement the count because the substring is shrinking from the left
                count -= 1 if s[pointerA] in vowelSet else 0
                
                # Move the start of the substring (pointerA) to the right
                pointerA += 1
            
            # Update the result to be the maximum of the current result and count
            result = max(result, count)
        
        # Return the maximum count of vowels in any valid substring of length k
        return result

# Example usage:
solution_instance = Solution()
s = "leetcode"
k = 3
result = solution_instance.maxVowels(s, k)
print(result)  # Output will be 2
