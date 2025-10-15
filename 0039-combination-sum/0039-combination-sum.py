class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, path, total):
            # Base case: found a valid combination
            if total == target:
                res.append(path[:])
                return
            # Exceeded the target
            if total > target:
                return

            # Try each candidate starting from 'start' index
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # Recurse with same 'i' (since we can reuse numbers)
                backtrack(i, path, total + candidates[i])
                path.pop()  # undo last step

        backtrack(0, [], 0)
        return res
