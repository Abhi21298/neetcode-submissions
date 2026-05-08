class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:
            inter_sum = numbers[l] + numbers[r]
            if inter_sum == target:
                return [l + 1,  r + 1]
            
            if inter_sum < target:
                l = l + 1
            else:
                r = r - 1
               
        