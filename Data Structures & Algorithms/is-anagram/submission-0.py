class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        tracker_s, tracker_t = {}, {}

        for i in range(len(s)):
            tracker_s[s[i]] = tracker_s.get(s[i], 0) + 1
            tracker_t[t[i]] = tracker_t.get(t[i], 0) + 1
        
        for ch in tracker_s:
            if ch not in tracker_t or tracker_s[ch] != tracker_t[ch]:
                return False
        
        return True
        
        
        