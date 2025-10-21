class Solution:
    def permute(self, nums):
        result = []

        def backtrack(start):
            # Base case: if we've reached the end of the array
            if start == len(nums):
                result.append(nums[:])  # append a copy of current permutation
                return

            for i in range(start, len(nums)):
                # swap current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                # backtrack (undo the swap)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result
