class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        from collections import deque
        
        visited = set()
        q = deque([s])
        smallest = s
        
        def add_operation(s):
            s_list = list(s)
            for i in range(1, len(s), 2):  # add to odd indices
                s_list[i] = str((int(s_list[i]) + a) % 10)
            return ''.join(s_list)
        
        def rotate_operation(s):
            return s[-b:] + s[:-b]
        
        while q:
            cur = q.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            
            # Update smallest lexicographically
            if cur < smallest:
                smallest = cur
            
            # Apply operations
            added = add_operation(cur)
            rotated = rotate_operation(cur)
            
            # Add new states if not visited
            if added not in visited:
                q.append(added)
            if rotated not in visited:
                q.append(rotated)
        
        return smallest
