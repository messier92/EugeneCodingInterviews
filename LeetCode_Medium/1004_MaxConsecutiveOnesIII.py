"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

def longestOnes(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Brute force solution:
        # 1. Iterate through the list and check if it is 0 or 1 
        # 2. If it is 0, replace with 1 and subtract from k
        # 3. Repeat until all k's are used
        # 4. Count the longest length number of 1's in the array
        # 5. Repeat for each combination
        # Time complexity (O^k) where this must be repeated for the value of k
        # Space complexity O(1) no extra space needed

        # Two pointers solution
        # Use a sliding window between index A and index B
        # Increase index B at every iteration
        # If the value of the index is 0, subtract from K until K is 0
        # Once all K = 0, get the maximum consecutive Ones
        # Time complexity (O(n)) since each element is visited at most twice
        # Space complexity O(1)

        left = 0
        right = 0
        maxconsec = 0
        count = 0

        for right in range(len(nums)):
            # increase count when it encounters a 0
            if nums[right] == 0:
                count += 1
            while count > k:
                # if count is greater than k, reclaim a count and move the left window forward
                if nums[left] == 0:
                    count -= 1
                left += 1
            # calculate the maximum consecutive
            maxconsec = max(maxconsec,right-left+1)
            print(maxconsec)

        return maxconsec
                
      

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums,k))

'''
How this works:
if the value of k is greater than the number of 0's in the list, it will never hit the "while count > k:" part
right will just keep increasing and left will stay at 0, so the final equation will be 
maxconsec = max(0,len(nums)-0+1)

However, if the value of k is lesser than the number of 0's in the list, we check the leftmost value of the window
if it is a 1, we just move the pointer forward until it counters a 0
then we reclaim a count
maxconsecutive will always update at every tick and replaces itself once it finds a new max number
'''