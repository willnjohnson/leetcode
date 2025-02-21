class Solution:
    def isHappy(self, n: int) -> bool:
        # Cycle detection
        seen_set = set()

        # Stop when condition hits 1
        while (n != 1):
            # Or if there's a cycle return False
            if n in seen_set:
                return False
            seen_set.add(n)
            
            total = 0
            while n > 0:
                digit = n % 10
                total += digit**2
                n //= 10
            
            n = total
        
        return True # case when condition == 1