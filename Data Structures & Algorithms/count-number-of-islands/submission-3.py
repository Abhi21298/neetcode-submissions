class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        R, C = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def dfs(r, c):

            if r not in range(R) or \
                c not in range(C) or \
                grid[r][c] != '1' or \
                (r, c) in visit:
                return
            
            visit.add((r, c))

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)


        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1' and (r,c) not in visit:
                    islands += 1
                    dfs(r, c)
        
        return islands