class Solution:
    def solveSudoku(self, board):
        def valid(row, col, num):
            for i in range(9):
                if board[row][i] == num:
                    return False
                if board[i][col] == num:
                    return False
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            return True
        def solve():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for num in "123456789":
                            if valid(row, col, num):
                                board[row][col] = num
                                if solve():
                                    return True
                                board[row][col] = "."
                        return False
            return True
        solve()
