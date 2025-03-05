class Solution:
    def calculate(self, s: str) -> int:
        result, sign, current_number, stack = 0, 1, 0, []
        
        for char in s:
            if char.isdigit():
                # Build current number from string
                current_number = current_number * 10 + int(char)
            elif char in '+-':
                result += sign * current_number     # Apply previous operation
                current_number = 0                  # Reset current number
                sign = 1 if char == '+' else -1     # Set new sign
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result, sign = 0, 1                 # Reset for sub-expression
            elif char == ')':
                result += sign * current_number
                current_number = 0
                result *= stack.pop()               # Pop sign
                result += stack.pop()               # Pop previous result
        
        result += sign * current_number             # Add the last number

        return result
