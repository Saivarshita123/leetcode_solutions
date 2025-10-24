class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0

        return max_sum
