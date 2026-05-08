class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        resLen = float("inf")
        l, r = 0, 0
        track_sum = 0

        while l <= r and r < len(nums):

            track_sum += nums[r]

            while track_sum >= target:
                resLen = min(r - l + 1, resLen)
                track_sum -= nums[l]
                l += 1
            
            r += 1
        
        return resLen if resLen != float("inf") else 0





