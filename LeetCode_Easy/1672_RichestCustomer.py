class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maximum_wealth = 0
        for account in accounts:
            curr_wealth = sum(account)
            maximum_wealth = max(maximum_wealth, curr_wealth)

        return maximum_wealth
    
solution_instance = Solution()
accounts = [[1,2,3],[3,2,1]]

result = solution_instance.maximumWealth(accounts)
# Print the result
print(result)