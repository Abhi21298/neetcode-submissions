class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        actual_total = (n * (n + 1)) // 2
        calc_total = sum(nums)  
        
        if actual_total == calc_total:
            return 0
        
        return abs(calc_total - actual_total)

        