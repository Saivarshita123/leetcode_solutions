class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1

        # Person 0 shares secret with firstPerson at time 0
        union(0, firstPerson)

        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])

        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            temp = []

            # Process all meetings at the same time
            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                union(x, y)
                temp.append((x, y))
                i += 1

            # Check which components are connected to person 0
            root0 = find(0)
            connected = set()
            for x, y in temp:
                if find(x) == root0 or find(y) == root0:
                    connected.add(find(x))
                    connected.add(find(y))

            # Rollback unions for people not connected to secret
            for x, y in temp:
                if find(x) not in connected:
                    parent[x] = x
                    parent[y] = y

        # Collect all people who know the secret
        root0 = find(0)
        return [i for i in range(n) if find(i) == root0]
