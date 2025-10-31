import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Regular expression that matches valid numbers
        pattern = re.compile(r'^[+-]?((\d+(\.\d*)?)|(\.\d+))([eE][+-]?\d+)?$')
        return bool(pattern.match(s.strip()))
