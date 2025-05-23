class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        r, c = 0, len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            val = matrix[r][c]
            
            if val == target:
                return True
            elif val > target:
                c -= 1  # Left
            else:
                r += 1  # Down

        return False