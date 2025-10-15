class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            temp = ""
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                temp += str(count) + s[i]
                i += 1
            s = temp
        return s
