class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        length = 1
        for n in nums:
            while length + n in nums:
                length += 1
            longest = max(length, longest)
            length = 1
        
        return longest


        