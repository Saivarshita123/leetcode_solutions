class Solution:
    def combine(self, n: int, k: int):
        res = []
        path = []
        
        def backtrack(start):
            # Base case: if the current combination is complete
            if len(path) == k:
                res.append(path[:])  # append a copy
                return
            
            # Choose next elements
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1)  # move to the next number
                path.pop()        # undo choice (backtrack)
        
        backtrack(1)
        return res
