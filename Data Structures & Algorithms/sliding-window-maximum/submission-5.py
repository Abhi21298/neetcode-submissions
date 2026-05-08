class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ## monotonically decreasing queue
        q = deque()
        l = 0
        result = []
        for r in range(len(nums)):

            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)
            if l > q[0]:
                q.popleft()
            
            if r - l + 1 >= k:
                result.append(nums[q[0]])
                l += 1
        
        return result
