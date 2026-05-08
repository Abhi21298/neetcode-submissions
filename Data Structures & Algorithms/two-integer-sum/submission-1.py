class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if not nums or len(nums) < 2:
            return nums
        
        track = {}
        for idx, el in enumerate(nums):
            if target - el in track:
                return [track[target - el] , idx]
            else:
                track[el] = idx
        
        return []
            
        
        