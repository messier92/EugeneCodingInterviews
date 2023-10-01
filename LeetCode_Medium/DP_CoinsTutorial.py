# Given a set of coin values coins={c1,c2,...,ck} and a target sum of money m, what's the minimum number of coins that form the sum m?

# Solution(0) = 0
# Solution(m) = min solution(m-c)+1
# Time complexity: O(M*K)

def min_ignore_none(a,b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a,b)

### Memoization ###
def minimum_coins(m, coins):
    if m in memo:
        return memo[m]
    
    if m == 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            subproblem = m - coin
            # skip solutions where m is negative
            if subproblem < 0:
                continue
            answer = min_ignore_none(answer, minimum_coins(subproblem, coins)+1)

    memo[m]  = answer
    return answer

### Bottom-up approach ###
def minimum_coins(m, coins):
    memo = {}
    memo[0] = 0
    for i in range(1, m+1):
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = min_ignore_none(memo[i], memo[subproblem] + 1)
    return memo[m]

