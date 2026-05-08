class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visit = set()
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        def bfs(r, c):
            if r not in range(rows) or \
                c not in range(cols) or \
                (r, c) in visit or \
                grid[r][c] == -1:
                return 
            
            visit.add((r,c))
            q.append([r, c])

        ## record the treasures in queue first
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append([r, c])
        
        dist = 0
        
        while q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()
                grid[r][c] = dist
                bfs(r + 1, c)
                bfs(r, c + 1)
                bfs(r - 1, c)
                bfs(r, c - 1)
            dist += 1

        

