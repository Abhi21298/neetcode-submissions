class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        counts = 0
        visit = set()

        graph = {i:[] for i in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(edge):

            if edge in visit:
                return
            
            visit.add(edge)
            for nei in graph[edge]:
                dfs(nei)
        
        for e in range(n):
            if e not in visit:
                counts += 1
                dfs(e)
        
        return counts