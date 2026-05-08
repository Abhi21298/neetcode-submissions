class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if nums == [] or len(nums) == 1:
            return False

        tracker = {}
        for i in nums:
            if i in tracker:
                return True
            else:
                tracker[i] = 1

        return False        