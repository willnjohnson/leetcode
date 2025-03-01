class Solution:
    def isValid(self, s: str) -> bool:
        # Use stack to track push and pop
        # Empty stack == Valid brackets
        stack = []
        
        # Iterate through each character of string
        for char in s:
            # Push upon opening bracket
            if char in "({[":
                stack.append(char)
            else:
                # Closing bracket but stack is empty
                if not stack:
                    return False
                
                # Pop upon matching closing bracket
                top = stack.pop()
                if char == ')' and top != '(':
                    return False
                if char == '}' and top != '{':
                    return False
                if char == ']' and top != '[':
                    return False
        
        # True if stack is empty, else false
        return not stack
