# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxone = 0
    counter = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            counter+=1
            if counter > maxone:
                maxone = counter
        else:
            counter = 0
                
    return maxone

nums = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))       