class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        winS, winT = {}, {}
        l = 0

        for c in t:
            winT[c] = winT.get(c, 0) + 1
        
        have, need = 0, len(winT)
        res, resLen = -1, float('inf')

        for r in range(len(s)):
            winS[s[r]] = winS.get(s[r], 0) + 1

            if s[r] in winT and winS[s[r]] == winT[s[r]]:
                have += 1
            
            while have == need:

                if r - l + 1 < resLen:
                    res = l
                    resLen = r - l + 1
                
                winS[s[l]] -= 1
                if s[l] in winT and winS[s[l]] < winT[s[l]]:
                    have -= 1
                
                l += 1
        
        return s[res: res + resLen] if resLen != float('inf') else ""