class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        L = len(nums)
        buckets = [[] for _ in range(L + 1)]
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        for key in counts:
            buckets[counts[key]].append(key)

        result = []

        while L >= 0:

            if buckets[L]:
                for i in buckets[L]:
                    if k <= 0:
                        return result
                    result.append(i)
                    k -= 1
            
            L -= 1
        
        return result

            