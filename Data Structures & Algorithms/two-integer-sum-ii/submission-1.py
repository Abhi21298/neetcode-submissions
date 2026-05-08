class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if numbers == "":
            return []
        l = len(numbers)
        if l < 2:
            return []
        
        i, j = 0, l - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        