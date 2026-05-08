import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = list()
        for a, b in points:
            dist = math.sqrt((a ** 2) + (b ** 2))
            distances.append((dist, a, b))
        
        heapq.heapify(distances)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(distances)
            res.append([x, y])
        
        return res