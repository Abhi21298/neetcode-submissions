class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        tracker = dict()

        for num in nums:
            tracker[num] = tracker.get(num, 0) + 1
        
        tracker = sorted(tracker.items(), key = lambda x: x[1], reverse=True)

        return list(int(tracker[i][0]) for i in range(k)) if k < len(tracker) \
            else list(int(tracker[i][0]) for i in range(len(tracker)))

    
        