class Solution:
    def countValidSelections(self, nums):
        n = len(nums)
        valid = 0

        def simulate(start, direction):
            arr = nums[:]  # make a copy
            curr = start
            dir = direction

            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += dir
                else:
                    arr[curr] -= 1
                    dir *= -1
                    curr += dir

            return all(x == 0 for x in arr)

        for i in range(n):
            if nums[i] == 0:
                if simulate(i, 1):   # move right
                    valid += 1
                if simulate(i, -1):  # move left
                    valid += 1

        return valid
