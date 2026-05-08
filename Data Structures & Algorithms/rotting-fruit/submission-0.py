class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh, time = 0, 0
        visit = set()
        q = deque()
        rows, cols = len(grid), len(grid[0])

        def rot(r, c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c] == 0:
                return

            visit.add((r,c))
            q.append([r, c])
            nonlocal fresh
            fresh -= 1    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:

                    visit.add((r,c))
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                rot(r, c + 1)
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c - 1)
            time += 1

        return time if fresh == 0 else -1


                