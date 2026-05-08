class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if nums == [] or len(nums) <= 1:
            return False

        track = set()
        for n in nums:
            if n in track:
                return True
            track.add(n)
        
        return False

        