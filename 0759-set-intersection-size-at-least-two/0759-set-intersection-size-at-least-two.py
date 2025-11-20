class Solution:
    def intersectionSizeTwo(self, intervals):
        # sort by end ascending, start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # a < b : the two largest chosen points so far
        a = b = -10**18
        ans = 0
        
        for l, r in intervals:
            if l > b:
                # no points in [l, r]
                a, b = r - 1, r
                ans += 2
            elif l > a:
                # exactly one point (b) in [l, r]
                a, b = b, r
                ans += 1
            else:
                # both a and b are inside [l, r], do nothing
                continue
        
        return ans
