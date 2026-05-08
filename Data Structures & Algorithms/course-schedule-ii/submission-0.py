class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
            
        output = []
        cycle = set()
        visit = set()

        def dfs(crs):

            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            output.append(crs)
            visit.add(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output
