class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        L= len(s)

        for i in range(L):

            l, r = i, i
            while l >= 0 and r < L and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < L and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res