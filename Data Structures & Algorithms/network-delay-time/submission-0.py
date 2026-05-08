class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append([v, w])
        
        visit = set()
        t = 0
        minH = [[0, k]]

        while minH:
            cost, node = heapq.heappop(minH)

            if node in visit:
                continue
            
            visit.add(node)
            t = cost

            for nei, time in graph[node]:
                if nei not in visit:
                    heapq.heappush(minH, [time + cost, nei])
        
        return t if len(visit) == n else -1
        
        