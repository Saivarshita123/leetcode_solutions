class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(start, path):
            res.append(path[:])  # store a copy of the current subset

            for i in range(start, len(nums)):
                path.append(nums[i])       # include nums[i]
                backtrack(i + 1, path)     # move forward
                path.pop()                 # backtrack (remove last)

        backtrack(0, [])
        return res
