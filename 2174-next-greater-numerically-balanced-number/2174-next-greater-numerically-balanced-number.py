class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # Helper function to check if a number is numerically balanced
        def isBalanced(num):
            from collections import Counter
            count = Counter(str(num))
            for digit, freq in count.items():
                if int(digit) != freq:
                    return False
            return True
        
        # Start searching from n + 1
        i = n + 1
        while True:
            if isBalanced(i):
                return i
            i += 1
