class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        
        res = 0

        for n in nums:
            if n - 1 not in nums:
                length = 1
                while n + length in nums:
                    length += 1
                
                res = max(res, length)
        
        return res