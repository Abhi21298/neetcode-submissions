import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = collections.Counter(tasks)
        heap = [-ct for ct in count.values()]

        q = deque()
        heapq.heapify(heap)
        time = 0
        while heap or q:
            time += 1
            if heap:
                val = 1 + heapq.heappop(heap)
                if val != 0:
                    q.append([val, time + n])
            
            if q and q[0][1] == time:
                v, _ = q.popleft()
                heapq.heappush(heap, v)
            
        return time