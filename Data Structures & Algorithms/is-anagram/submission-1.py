class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        track_s = {}
        track_t = {}
        for i in range(len(s)):
            track_s[s[i]] = track_s.get(s[i], 0) + 1
            track_t[t[i]] = track_t.get(t[i], 0) + 1

        for ch in track_t:
            if ch not in track_s or track_s[ch] != track_t[ch]:
                return False
        
        return True
        