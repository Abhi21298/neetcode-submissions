from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s: 
            return 0
        

        l, r = 0, 0
        tracker = defaultdict(int)
        resLen, maxf = 0, 1

        while r < len(s):
            
            tracker[s[r]] += 1
            maxf = max(maxf, tracker[s[r]])
                
            while (r - l + 1) - maxf > k:
                tracker[s[l]] -= 1
                l += 1
            
            resLen = max(resLen, r - l + 1)
            r += 1
        
        return resLen



        