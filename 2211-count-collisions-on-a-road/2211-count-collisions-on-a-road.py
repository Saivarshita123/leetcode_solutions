class Solution:
    def countCollisions(self, directions: str) -> int:
        # Remove cars that will never collide
        l = 0
        while l < len(directions) and directions[l] == 'L':
            l += 1

        r = len(directions) - 1
        while r >= 0 and directions[r] == 'R':
            r -= 1

        # Count all moving cars ('L' or 'R') inside the remaining section
        collisions = 0
        for i in range(l, r + 1):
            if directions[i] != 'S':
                collisions += 1

        return collisions
