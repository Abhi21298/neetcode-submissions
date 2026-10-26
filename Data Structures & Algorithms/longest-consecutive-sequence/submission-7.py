class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 0
        nums = set(nums)

        for n in nums:
            
            if n - 1 not in nums:
                inter_len = 1

                while n + inter_len in nums:
                    inter_len += 1
            
                res = max(res, inter_len)

        return res