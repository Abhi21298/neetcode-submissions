class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        counts = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        for num, freq in counts.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                if k == 0:
                    return res
                k -= 1
                res.append(n)
        
        return res