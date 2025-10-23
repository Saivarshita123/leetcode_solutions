class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diagonals1, diagonals2):
         
            if row == n:
                self.count += 1
                return
            
            for col in range(n):
                d1 = row - col
                d2 = row + col
                
                # Skip if column or diagonal is under attack
                if col in cols or d1 in diagonals1 or d2 in diagonals2:
                    continue
                
                # Choose
                cols.add(col)
                diagonals1.add(d1)
                diagonals2.add(d2)
                
                # Explore next row
                backtrack(row + 1, cols, diagonals1, diagonals2)
                
                # Backtrack
                cols.remove(col)
                diagonals1.remove(d1)
                diagonals2.remove(d2)
        
        self.count = 0
        backtrack(0, set(), set(), set())
        return self.count
