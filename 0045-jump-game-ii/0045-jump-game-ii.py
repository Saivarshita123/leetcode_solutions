class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        jumps = 0
        farthest = 0
        current_end = 0
        
        # We don't need to jump from the last index
        for i in range(n - 1):
            # Keep track of the farthest point reachable so far
            farthest = max(farthest, i + nums[i])
            
            # If we reach the end of the current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
                
        return jumps
