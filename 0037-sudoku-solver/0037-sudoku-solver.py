class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize sets and list of empty cells
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    empty.append((i, j))
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)

        def backtrack(k=0):
            if k == len(empty):
                return True  # solved
            
            i, j = empty[k]
            b = (i // 3) * 3 + (j // 3)

            for ch in '123456789':
                if ch not in rows[i] and ch not in cols[j] and ch not in boxes[b]:
                    # Place the number
                    board[i][j] = ch
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[b].add(ch)

                    if backtrack(k + 1):
                        return True

                    # Undo the move
                    board[i][j] = '.'
                    rows[i].remove(ch)
                    cols[j].remove(ch)
                    boxes[b].remove(ch)

            return False

        backtrack()
