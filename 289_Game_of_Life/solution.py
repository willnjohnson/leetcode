class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                live_neighbors = sum((0 <= i + dx < m and 0 <= j + dy < n and board[i + dx][j + dy] & 1) for dx, dy in dir)
                
                if board[i][j] == 1:
                    if live_neighbors not in [2, 3]:
                        board[i][j] = 1
                    else:
                        board[i][j] = 3
                elif live_neighbors == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1