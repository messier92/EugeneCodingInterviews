# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Hint - Implement Fibonnaci using DP

def climbStairs(n):
    # base case
    if n <= 2:
        return n
    # create an array of size n+1
    dp = [0] * (n+1)
    # default the first 2 index to be 1 and 2 respectively 
    dp[1], dp[2] = 1, 2
    # calculate from the 3rd index onwards
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    # return the value 
    return dp[n]

steps = 10
print(climbStairs(steps))