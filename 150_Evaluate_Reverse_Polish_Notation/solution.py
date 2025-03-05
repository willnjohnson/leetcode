class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in '+-*/':
                # Pop operands in reverse order (a, b)
                b, a = stack.pop(), stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
            else:
                # Convert token to integer and push it to stack
                stack.append(int(token))
        
        return stack.pop()
