class Solution:
    def longestPalindrome(self, s: str) -> str:
        # base case
        if not s:
            return ''
        # init n to be the length of the string
        n = len(s)
        # initialize the dp table to be false for the length of the string
        dp = [[False] * n for _ in range(n)]        
        ans = [0,0]

        # set all dp[i][i] to true
        for i in range(n):
            dp[i][i] = True

        # iterate over all pairs i, i+1
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i, i+1]
        
        # for diff in range 2 to length of the string
        for diff in range(2,n):
            for i in range(n-diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i, j]
        i, j = ans
        return s[i:j+1]

# Create an instance of the Solution class
solution_instance = Solution()
# Define palindrome
word = "ababa"
# Call the longestPalindrome method on the solution_instance
result = solution_instance.longestPalindrome(word)
# Print the result
print(result)
