class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sorting is crucial to handle duplicates
        anslist = []

        def backtrack(start, path, target):
            if target == 0:
                anslist.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # If the current number is greater than the remaining target, 
                # no need to check further because the list is sorted.
                if candidates[i] > target:
                    break
                
                # Skip duplicates: if the current number is the same as the previous 
                # one in the same recursive level, skip it to avoid duplicate sets.
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Move to 'i + 1' because each number can be used only once
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])     

        backtrack(0, [], target)
        return anslist
    