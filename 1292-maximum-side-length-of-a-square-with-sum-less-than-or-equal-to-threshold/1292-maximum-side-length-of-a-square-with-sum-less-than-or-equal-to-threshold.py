from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Step 1: Build prefix sum
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre[i + 1][j + 1] = (
                    mat[i][j]
                    + pre[i][j + 1]
                    + pre[i + 1][j]
                    - pre[i][j]
                )

        # Function to check if square of size k exists
        def exists(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    total = (
                        pre[i + k][j + k]
                        - pre[i][j + k]
                        - pre[i + k][j]
                        + pre[i][j]
                    )
                    if total <= threshold:
                        return True
            return False

        # Step 2: Binary search on side length
        left, right = 0, min(m, n)
        while left < right:
            mid = (left + right + 1) // 2
            if exists(mid):
                left = mid
            else:
                right = mid - 1

        return left
