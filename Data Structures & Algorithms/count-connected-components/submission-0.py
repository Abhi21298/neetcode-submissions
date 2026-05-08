class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visit = set()
        graph = {node:[] for node in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):

            if node in visit:
                return
            
            visit.add(node)
            for neighbours in graph[node]:
                dfs(neighbours)
        
        counts = 0
        for node in graph:
            if node in visit:
                continue
            else:
                counts += 1
                dfs(node)
        
        return counts

        