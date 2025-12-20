class Solution:
    def minDeletionSize(self, strs):
        rows = len(strs)
        cols = len(strs[0])
        delete_count = 0

        for c in range(cols):
            for r in range(rows - 1):
                if strs[r][c] > strs[r + 1][c]:
                    delete_count += 1
                    break

        return delete_count
