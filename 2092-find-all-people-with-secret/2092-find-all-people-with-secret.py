class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
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
            involved = []

            # Union all meetings at the same time
            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                union(x, y)
                involved.append(x)
                involved.append(y)
                i += 1

            # Keep only components connected to person 0
            root0 = find(0)
            for person in involved:
                if find(person) != root0:
                    parent[person] = person

        # Collect all people who know the secret
        root0 = find(0)
        return [i for i in range(n) if find(i) == root0]
