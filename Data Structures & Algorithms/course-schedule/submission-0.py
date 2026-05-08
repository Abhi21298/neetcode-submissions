class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {}
        visit = set()

        # Course mapping with list of prerequisites
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        
        # DFS to look through course
        def dfs(crs):

            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in preMap[crs]:

                if not dfs(pre): return False
            
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        # call for each course as there might be disconnected graphs
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True