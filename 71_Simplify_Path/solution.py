class Solution:
    def simplifyPath(self, path: str) -> str:
        segments = path.split('/')
        stack = []
        
        for segment in segments:
            if segment == '' or segment == '.':
                # Ignore empty or current directory (.)
                continue
            elif segment == '..':
                # Parent directory (..), pop from stack
                if stack:
                    stack.pop()
            else:
                # Valid directory name, push it onto the stack
                stack.append(segment)
        
        # Join stack into simplified path
        return '/' + '/'.join(stack)