# Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.
# Return the length of n. If there is no such n, return -1.
# Note: n may not fit in a 64-bit signed integer.

# We want to find the shortest number made only of digits "1" that is divisible by k.
# 1,11,111,1111,11111,11111, etc...
# Instead of storing the full number, we keep only its remainder mod k
# You want to find a number that:
# Is made only of the digit 1 (like 1, 11, 111, 1111, …) 
# And is divisible by k 
# And you want the shortest such number.

# Example:
# If k = 3, the smallest number made only of 1s that is divisible by 3 is:
# 111   → divisible by 3
# If k = 4, find the LENGTH of the smallest number of repunit that is divisible by 4


def smallestRepunitDivByK(k):
    """
    :type k: int
    :rtype: int
    """
    if (k%2==0 or k%5==0):
        return -1

    remainder = 0
    # starts from 11 as any number below this is covered by 2 and 5
    for length in range(1,k+1):
        remainder=(remainder*10+1)%k
        print("K: " + str(k))
        print("Remainder: " + str(remainder))

        if remainder==0:
            return length

    return -1

k = 7
print(smallestRepunitDivByK(7))