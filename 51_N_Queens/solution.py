class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.n = n
        self.backtrack(0, [], set(), set(), set())
        return self.res

    def backtrack(self, row, stack, cols, diag1, diag2):
        if row == self.n:
            board = [''.join('Q' if c == col else '.' for c in range(self.n)) for col in stack]
            self.res.append(board)
            return
        for col in range(self.n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            stack.append(col)
            self.backtrack(row + 1, stack, cols | {col}, diag1 | {row - col}, diag2 | {row + col})
            stack.pop()