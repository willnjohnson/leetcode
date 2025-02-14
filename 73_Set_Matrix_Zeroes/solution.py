class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        """
        Modify matrix in-place by setting the entire row and column to zero if an element is 0.
        
        Time Complexity: O(m*n)
        Space Complexity: O(1)
        """
        rows, cols = len(matrix), len(matrix[0])
        
        # Collect positions of all zeros
        zero_positions = [(i, j) for i in range(rows) for j in range(cols) if matrix[i][j] == 0]
        
        # Set the entire row and column to zero for each zero position
        for i, j in zero_positions:
            for row in range(rows):
                matrix[row][j] = 0
            for col in range(cols):
                matrix[i][col] = 0
