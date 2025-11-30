class Solution:
    def minSubarray(self, nums, p):
        total = sum(nums) % p
        if total == 0:
            return 0

        prefix = 0
        mod_index = {0: -1}  # prefix sum mod -> last index
        min_len = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            needed = (prefix - total) % p
            if needed in mod_index:
                min_len = min(min_len, i - mod_index[needed])
            mod_index[prefix] = i

        return min_len if min_len < len(nums) else -1
