class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # if not edges or len(edges) == 0:
        #     return 1
        
        graph = {i:[] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visit = set()
        cts = 0

        def dfs(node):

            if node in visit:
                return
            

            visit.add(node)
            for neigh in graph[node]:
                dfs(neigh)
        
        for n in graph:
            if n not in visit:
                dfs(n)
                cts += 1
        
        return cts
        