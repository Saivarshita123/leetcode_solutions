class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        # Step 1: Check if first row or column has any zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Step 2: Use first row/col as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 3: Set zeroes based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 4: Handle first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Step 5: Handle first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
