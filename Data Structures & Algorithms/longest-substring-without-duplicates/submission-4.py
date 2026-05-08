class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        track = set()
        length = 0
        l = 0

        for r in range(len(s)):
            
            while s[r] in track:
                track.remove(s[l])
                l = l + 1
            
            track.add(s[r])
            length = max(length, r - l + 1)
        
        return length
                


        