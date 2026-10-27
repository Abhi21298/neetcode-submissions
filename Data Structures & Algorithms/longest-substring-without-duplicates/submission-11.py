class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        track = set()
        reslen, l = 0, 0

        for r in range(len(s)):

            while track and s[r] in track:
                track.remove(s[l])
                l += 1
            
            track.add(s[r])
            reslen = max(reslen, r - l + 1)
        
        return reslen
