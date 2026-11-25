from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        ## combo of maxheap and queue 
        tracker = Counter(tasks)

        maxHeap = [-cnt for cnt in tracker.values()]
        heapq.heapify(maxHeap) ## how to prioritise tasks here

        q = deque() ## to keep track of which task is available first and operate
        t = 0

        while q or maxHeap:

            t += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, t + n])
            
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return t


        
        