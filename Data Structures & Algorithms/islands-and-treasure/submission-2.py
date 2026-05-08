class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visit = set()
        rows, cols = len(grid), len(grid[0])
        q = deque()

        def addIsland(r, c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c] == -1:
                return
            
            visit.add((r, c))
            q.append([r, c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:

                    visit.add((r, c))
                    q.append([r, c])
        
        dist = 0
        while q:
            for i in range(len(q)):

                r, c = q.popleft()
                grid[r][c] = dist
                addIsland(r + 1, c)
                addIsland(r - 1, c)
                addIsland(r, c - 1)
                addIsland(r, c + 1)
            dist += 1


        

        

        

