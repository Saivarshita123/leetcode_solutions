class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()  # Important: sort to handle duplicates
        result = []
        subset = []

        def backtrack(index):
            result.append(subset.copy())

            for i in range(index, len(nums)):
                # Skip duplicate values at the same recursive level
                if i > index and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return result
