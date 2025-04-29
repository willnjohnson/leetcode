class Solution:
    def __init__(self):
        # Memoization dictionary
        self.memo = {}

    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Return expression that's been computed
        if expression in self.memo:
            return self.memo[expression]
        
        # Return expression as list if is numeric
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        # Loop through expression and split at each operator
        for i in range(len(expression)):
            if expression[i] in "+-*":
                # Split expression into two parts (left and right)
                l = expression[:i]
                r = expression[i+1:]
                
                # Recursively compute the results for both parts
                l_results = self.diffWaysToCompute(l)
                r_results = self.diffWaysToCompute(r)
                
                # Combine results of the two parts
                for l in l_results:
                    for r in r_results:
                        if expression[i] == '+':
                            results.append(l + r)
                        elif expression[i] == '-':
                            results.append(l - r)
                        elif expression[i] == '*':
                            results.append(l * r)

        # Store computed result in memoization dictionary
        self.memo[expression] = results
        return results