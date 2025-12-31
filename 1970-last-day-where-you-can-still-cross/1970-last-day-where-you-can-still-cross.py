from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:

        def canCross(day):
            # 0 = land, 1 = water
            grid = [[0] * col for _ in range(row)]

            # flood cells up to 'day'
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1

            queue = deque()

            # start from all land cells in top row
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    grid[0][c] = 1  # mark visited

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            while queue:
                r, c = queue.popleft()

                # reached bottom row
                if r == row - 1:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))

            return False

        left, right = 0, row * col
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if canCross(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
