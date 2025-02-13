class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Strategy:         Traverse through matrix via sliding window in spiral order by managing four boundaries (top, bottom, left, right).
        # Time Complexity:  O(m * n) where m is the number of rows and n is the number of columns. Every element is visited once.


        res = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            for j in range(left, right + 1):  # Traverse top row
                res.append(matrix[top][j])
            top += 1
            
            for i in range(top, bottom + 1):  # Traverse right column
                res.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                for j in range(right, left - 1, -1):  # Traverse bottom row
                    res.append(matrix[bottom][j])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):  # Traverse left column
                    res.append(matrix[i][left])
                left += 1
        
        return res