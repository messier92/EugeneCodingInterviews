class Solution:
    def partitionString(self, s: str) -> int:
        # Initialize an empty result string to store unique partitions
        result = ""
        
        # Initialize a count to keep track of the number of partitions
        count = 0
        
        # Iterate through each letter in the input string 's'
        for letter in s:
            # Check if the letter is already in the 'result' string
            if letter in result:
                # Reset the 'result' string as a new partition is starting
                result = ""
                # Increment the count as a new partition has been detected
                count += 1
            
            # Append the current letter to the 'result' string
            result += letter
        
        # Check if the length of the 'result' string is not zero (indicating there's a single character left)
        if len(result) != 0:
            # Increment the count to account for the last partition
            count += 1
        
        # Return the total count of partitions
        return count

# Example usage:
solution_instance = Solution()
s = "abacaba"
result = solution_instance.partitionString(s)
print(result)  # Output will be 4
