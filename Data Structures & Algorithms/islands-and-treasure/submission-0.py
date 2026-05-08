class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # bfs approach

        visit = set()
        q = deque()
        rows, cols = len(grid), len(grid[0])

        ## actual bfs checking code
        def addRoom(r, c):

            if (r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c] == -1):
                return
            
            visit.add((r, c))
            q.append([r, c])

        # starting with gates == starting nodes which we usually add in queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: ## record the gates first in visited and queue
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0

        ### now pop layer by layer and update distance after every layer is done!    
        while q:
        
            for i in range(len(q)):

                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r, c + 1)
                addRoom(r - 1, c)
                addRoom(r, c - 1)
            dist += 1
        

         
        