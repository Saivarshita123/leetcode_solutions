class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])

        # sorted_ok[i] = True means strs[i] <= strs[i+1] already confirmed
        sorted_ok = [False] * (n - 1)
        deletions = 0

        for col in range(m):
            # Check if this column breaks order
            bad = False
            for i in range(n - 1):
                if not sorted_ok[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break

            if bad:
                deletions += 1
                continue

            # Update confirmed order
            for i in range(n - 1):
                if not sorted_ok[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_ok[i] = True

        return deletions
