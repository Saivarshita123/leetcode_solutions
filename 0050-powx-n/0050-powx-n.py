class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        
        while n > 0:
            # If n is odd, multiply result by current x
            if n % 2 == 1:
                result *= x
            # Square x
            x *= x
            # Divide exponent by 2
            n //= 2
        
        return result
