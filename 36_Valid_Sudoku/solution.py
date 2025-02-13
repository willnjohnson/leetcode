class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Time Complexity: O(1) – number of operations constant since grid is fixed
        Space Complexity: O(1) – space remains constant since three fixed size sets are utilized
        
        Strategy used:
        Backtracking (walk through the board and check rows, columns, sub boxes) - 
        - As we fill each cell, we check if it breaks rules
        - If a conflict occurs, stop and conclude board is invalid
        '''

        # Sets track seen numbers in rows, columns, and 3x3 sub-boxes
        rows, cols, sub_boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        
        # Traverse each cell in board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':  # Skip empty cells
                    continue
                
                # Calculate sub-box index
                sub_box_index = (i // 3) * 3 + (j // 3)
                
                # Check for conflicts
                if num in rows[i] or num in cols[j] or num in sub_boxes[sub_box_index]:
                    return False
                
                # Mark number as seen in respective row, column, and sub-box
                rows[i].add(num)
                cols[j].add(num)
                sub_boxes[sub_box_index].add(num)
        
        return True
