class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        tracker = {}
        l = 0
        length = 0
        
        #maxf = 0
        for r in range(len(s)):
            tracker[s[r]] = tracker.get(s[r], 0) + 1
            #maxf = max(maxf, tracker[s[r]])
            
            #while (r - l + 1) - maxf > k:
            while (r - l + 1) - max(tracker.values()) > k:
                tracker[s[l]] -= 1
                l += 1
            
            length = max(length, r - l + 1)
            
        
        return length
        