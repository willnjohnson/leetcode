class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialized variables
        m = [[0] * n for _ in range(n)]
        num = 1

        # Bounds
        left, right, top, bottom = 0, n - 1, 0, n - 1

        while left <= right and top <= bottom:
            # Left-right
            for i in range(left, right + 1):
                m[top][i] = num
                num += 1
            top += 1

            # Top-bottom
            for i in range(top, bottom + 1):
                m[i][right] = num
                num += 1
            right -= 1

            if top <= bottom:
                # Right-left
                for i in range(right, left - 1, -1):
                    m[bottom][i] = num
                    num += 1
                bottom -= 1

            if left <= right:
                # Bottom-top
                for i in range(bottom, top - 1, -1):
                    m[i][left] = num
                    num += 1
                left += 1

        return m
