from typing import List

# Define the Solution class
class Solution:
    def reverseStringInPlace(self, s: List[str]) -> List[str]:
        # define left and right pointers
        l = 0
        # you need to minus 1 from the right pointer to exclude the first element at index 0, otherwise you will get index out of range
        r = len(s) - 1

        # begin two pointers method
        while l < r:
            # swap the beginning and the last element of the list
            s[l], s[r] = s[r], s[l]
            # increment left pointer
            l+=1
            # decrease right pointer
            r-=1
        
        return s

# Create an instance of the Solution class
solution_instance = Solution()
# Define the input string list
input_string_list = ["h","e","l","l","o"]
# Call the reverseStringInPlace method on the solution_instance
result = solution_instance.reverseStringInPlace(input_string_list)
print(result)  
