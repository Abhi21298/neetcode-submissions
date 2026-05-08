class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        track = set(nums)
        longest = 0

        for n in track:
            if n - 1 not in track:
                length = 1
                while n + length in track:
                    length += 1
                
                longest = max(longest, length)
        
        return longest
        