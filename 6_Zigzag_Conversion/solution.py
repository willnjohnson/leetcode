from enum import Enum

class Direction(Enum):
    DOWN = 1
    UP = -1

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # One row or string is short, then return string
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list to store characters in each row
        rows = [''] * numRows
        current_row = 0
        direction = Direction.DOWN
        
        # Traverse through string
        for char in s:
            rows[current_row] += char

            # Change direction when top or bottom row is hit
            if current_row == 0:
                direction = Direction.DOWN 
            elif current_row == numRows - 1:
                direction = Direction.UP

            # Move to the next row
            current_row += direction.value
        
        # Join all rows and return zigzagged string
        return ''.join(rows)
