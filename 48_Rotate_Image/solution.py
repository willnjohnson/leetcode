class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        """        
        Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
        Step 2: Reverse each row to complete the rotation.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        
        # Step 1
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                # Swap elements across diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2
        for i in range(n):
            # Reverse each row in-place
            matrix[i].reverse()