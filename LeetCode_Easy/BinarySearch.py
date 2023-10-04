# Time complexity O(LogN)
# Space complexity O(1)
def binarySearch(arr, target):
    # init left pointer to be 0
    left = 0
    # init right pointer to be len(arr)-1
    right = len(arr) - 1

    # while left pointer has not overtaken right pointer
    while left <= right:
        # get the midpoint
        mid = (left+right) // 2
        # compare the number in the midpoint of the array
        if arr[mid] == target:
            return mid
        # if the current midpoint of the array is lesser than the target, increase the left pointer as it is on the left side
        elif arr[mid] < target:
            left = mid+1
        # if the current midpoint of the array is greater than the target, decrease the right pointer as it is on the right side
        else:
            right = mid-1
        # if it is found
    return -1
    
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target_element = 9
result = binarySearch(sorted_array, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print("Element not found in the array.")
