class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = {i:[] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visit = set()
        
        def dfs(course, prev):
            if course in visit:
                return False
            
            visit.add(course)
            for nei in graph[course]:
                if nei == prev:
                    continue
                if not dfs(nei, course):
                    return False
            
            return True
        
        return dfs(0, -1) and n == len(visit)
        