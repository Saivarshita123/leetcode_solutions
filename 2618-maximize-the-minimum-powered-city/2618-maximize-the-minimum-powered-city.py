class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)
        
        # Step 1: Precompute power for each city using prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stations[i]
            
        power = [0] * n
        for i in range(n):
            left = max(0, i - r)
            right = min(n - 1, i + r)
            power[i] = prefix[right + 1] - prefix[left]
        
        # Step 2: Check function for feasibility
        def can(minPower):
            add = [0] * (n + 1)
            added = 0
            curAdd = 0
            
            for i in range(n):
                curAdd += add[i]
                currentPower = power[i] + curAdd
                if currentPower < minPower:
                    need = minPower - currentPower
                    if added + need > k:
                        return False
                    added += need
                    curAdd += need
                    if i + 2 * r + 1 < n:
                        add[i + 2 * r + 1] -= need
            return True
        
        # Step 3: Binary search for maximum possible min power
        low, high = 0, sum(stations) + k
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
