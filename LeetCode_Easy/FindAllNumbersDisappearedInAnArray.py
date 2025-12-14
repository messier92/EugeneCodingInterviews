
def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # the index of the list corresponds to the element of the list
    # if it is present, it will be saved in nums as a negative value
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]

    result = []
    # if the number is not a negative value, return it
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)
        
    return result

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))