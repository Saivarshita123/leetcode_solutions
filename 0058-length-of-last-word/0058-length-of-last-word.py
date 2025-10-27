class Solution:
    def lengthOfLastWord(self, s: str) -> int:
  
        words = s.strip().split()
        # Return length of last word
        return len(words[-1])
