class Solution:
    def solveNQueens(self, n: int):
        def backtrack(row, cols, diagonals1, diagonals2, board):
            
            if row == n:
                result.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                # Calculate diagonals
                d1 = row - col
                d2 = row + col
                
                
                if col in cols or d1 in diagonals1 or d2 in diagonals2:
                    continue
                
                # Place queen
                board[row][col] = 'Q'
                cols.add(col)
                diagonals1.add(d1)
                diagonals2.add(d2)
                
                # Move to next row
                backtrack(row + 1, cols, diagonals1, diagonals2, board)
                
                # Remove queen (backtrack)
                board[row][col] = '.'
                cols.remove(col)
                diagonals1.remove(d1)
                diagonals2.remove(d2)
        
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return result
