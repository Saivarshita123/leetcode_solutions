class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def backtrack(i, dots, path):
            # If we formed 4 parts and used all digits
            if dots == 4 and i == len(s):
                res.append(path[:-1])  # remove last dot
                return

            # If 4 parts already but still digits left → invalid
            if dots == 4:
                return

            # Try to take 1 to 3 digits
            for j in range(i, min(i + 3, len(s))):
                segment = s[i:j+1]

                # Leading zero check
                if segment[0] == '0' and len(segment) > 1:
                    break

                # Range check
                if int(segment) <= 255:
                    backtrack(j+1, dots+1, path + segment + ".")
                else:
                    break

        backtrack(0, 0, "")
        return res
