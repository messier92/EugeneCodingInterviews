# Backtracking
# Define the problem and constraints
# Design the recursive function
# Define Base Case
# Make choices and explore
# Backtrack
# Optimize (optional)

def backtrack(start, subset, nums, subsets):
    # Add the current subset to the list of subsets
    subsets.append(subset[:])

    # Explore all possible choices from the current index
    for i in range(start, len(nums)):
        # append the current number combination to subset
        subset.append(nums[i])
        # backtrack
        backtrack(i+1, subset, nums, subsets)
        # remove the latest subset
        subset.pop()

def generate_subsets(nums):
    subsets = []
    backtrack(0, [], nums, subsets)
    return subsets


input_set = [1,2,3]
result = generate_subsets(input_set)
print(result)
