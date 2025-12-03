# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# use two pointers to solve
# find the highest in the left pointer and the highest in the right pointer where the distance is the greatest
# then multiply the x-axis of the lower one with the y-axis of the distance between the two points
# move the shorter one

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left = 0
    right = len(height) - 1
    maxWater = 0
        
    while left < right:
        if height[left] < height[right]:
            width = abs(right - left)       
            area = width*height[left]
            maxWater = max(maxWater, area)
            left += 1    
        else:
            width = abs(left - right)
            area = width*height[right]
            maxWater = max(maxWater, area)
            right -= 1
    return maxWater        


height = [1,8,6,2,5,4,8,3,7]
maxArea(height)