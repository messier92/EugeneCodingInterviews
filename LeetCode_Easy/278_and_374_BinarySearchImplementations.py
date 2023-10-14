### 374. Guess Number Higher or Lower ###
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # implement binary search
        # init left pointer to 0
        left = 1
        # init right pointer to be n (max)
        right = n
        # while left is less than or equal to right
        while left<=right:
            # get the midpoint
            mid = (left+right)//2
            # guess the midpoint and check if it is the correct one
            if guess(mid) == 0:
                return mid
            # if num < pick, shift left
            elif (guess(mid) == 1):
                left = mid+1
            # otherwise, shift right
            else:
                right = mid-1
        # return the left pointer
        return left

### 278. First Bad Version ###
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        result = 0

        while left <=right:
            mid = (left+right)//2
            if isBadVersion(mid) == True:
                result=mid
                right=mid-1
            else:
                left=mid+1
        return result
