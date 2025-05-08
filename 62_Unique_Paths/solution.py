class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        a, b = m + n - 2, min(m - 1, n - 1)
        result = 1
        for i in range(1, b + 1):
            result = result * (a - i + 1) // i
        return result
        '''

        # More efficient to use built-in math library
        return comb(m + n - 2, n - 1)