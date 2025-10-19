class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is zero
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize result array
        result = [0] * (len(num1) + len(num2))
        
        # Reverse strings to simplify indexing
        num1, num2 = num1[::-1], num2[::-1]
        
        # Multiply each digit
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit_mul = int(num1[i]) * int(num2[j])
                result[i + j] += digit_mul
                # Handle carry
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        # Convert back to string
        return ''.join(map(str, result[::-1]))
