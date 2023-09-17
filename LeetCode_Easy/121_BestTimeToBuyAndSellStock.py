from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # let the min_price be the first element of the list
        min_price = prices[0]
        # set the max profit at 0
        max_profit = 0
        # for each element in prices
        for price in prices:
            # if the element is less than the min_price, update min_price
            if price < min_price:
                min_price = price
            else:
                # if the element is more/equal to min price, get the max profit
                max_profit = max(max_profit, price - min_price)
        return max_profit

# Create an instance of the Solution class
solution_instance = Solution()
# Define your input list of prices
prices = [7, 1, 5, 3, 6, 4]
# Call the maxProfit method on the solution_instance
result = solution_instance.maxProfit(prices)
# Print the result
print(result)
