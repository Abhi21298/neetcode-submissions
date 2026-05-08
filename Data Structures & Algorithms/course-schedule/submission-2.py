class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        graph = {i:[] for i in range(numCourses)}
        visit = set()

        for a, b in prerequisites:
            graph[a].append(b)
        
        def dfs(course):

            if course in visit:
                return False
            # if graph[course] == []:
            #     return True

            visit.add(course)
            for each_pre in graph[course]:
                if not dfs(each_pre):
                    return False

            visit.remove(course)
            graph[course] = []
            return True 
        
        for each in range(numCourses):
            if not dfs(each):
                return False
        
        return True
        
        