class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        reslen = 1000001
        l, r = 0, 0
        inter_sum = 0

        while l <= r and r <= len(nums) - 1:
            inter_sum += nums[r]

            while inter_sum >= target:
                inter_sum -= nums[l]
                reslen = min(reslen, r - l + 1)
                l += 1

            r += 1
        
        return reslen if reslen != 1000001 else 0

