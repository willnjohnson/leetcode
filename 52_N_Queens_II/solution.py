class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self.n = n
        self.solve(0, set(), set(), set())
        return self.count

    def solve(self, row, cols, diag1, diag2):
        if row == self.n:
            self.count += 1
            return
        for col in range(self.n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            self.solve(row + 1, cols | {col}, diag1 | {row - col}, diag2 | {row + col})