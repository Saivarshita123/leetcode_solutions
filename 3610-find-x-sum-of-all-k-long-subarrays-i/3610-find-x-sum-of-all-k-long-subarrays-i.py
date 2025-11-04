from collections import Counter

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        ans = []
        
        for i in range(n - k + 1):
            window = nums[i:i+k]
            freq = Counter(window)
            
            # Sort by (-frequency, -value)
            top = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))[:x]
            top_elements = {num for num, _ in top}
            
            # Keep only elements in top x frequent
            total = sum(v for v in window if v in top_elements)
            ans.append(total)
        
        return ans
