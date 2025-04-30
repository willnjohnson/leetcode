class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Can use helper function with recursion, similar to functional programming approach
        def power(x, n):
            if n == 0:
                return 1  # Base case: x^0 = 1
            
            elif n < 0:
                x = 1 / x
                n = -n  # Handle negative

            # Recursive approach with exponentiation by squaring
            h = power(x, n // 2)
            
            if n % 2 == 0:
                return h * h
            else:
                return h * h * x
        
        return power(x, n)