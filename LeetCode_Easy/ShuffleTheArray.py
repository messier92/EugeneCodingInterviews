# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    pointer1 = 0
    pointer2 = n
    anslist = []
    while len(anslist) < 2*n:
        anslist.append(nums[pointer1])
        anslist.append(nums[pointer2])
        pointer1+=1
        pointer2+=1
    return anslist

nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums,n))        