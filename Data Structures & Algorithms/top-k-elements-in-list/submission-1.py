class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        track = defaultdict(int)
        counts = [[] for i in range(len(nums)+1)]

        for num in nums:
            track[num] += 1
        
        for num, cts in track.items():
            counts[cts].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            cts = counts[i] 
            if cts != []:
                for n in cts:
                    res.append(n)
                    k -= 1
                    if k == 0:
                        return res
         




        