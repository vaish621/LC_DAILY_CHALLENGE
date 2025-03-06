class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        st = (0, 0) 

        visited.add(st)

        for i in path:
            if i == 'N':
                st = (st[0], st[1] + 1)
            elif i == 'E':
                st = (st[0] + 1, st[1])
            elif i == 'S':
                st = (st[0], st[1] - 1)
            elif i == 'W':
                st = (st[0] - 1, st[1])

            if st in visited:
                return True
            visited.add(st)

        return False
