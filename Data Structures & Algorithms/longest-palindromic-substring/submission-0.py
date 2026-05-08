class Solution:
    def longestPalindrome(self, s: str) -> str:

        L = len(s)
        res = 0
        for i in range(len(s)):
            # odd length palindrome check
            l, r = i, i

            while l >= 0 and r < L and s[l] == s[r]:
                if r - l + 1 > res:
                    string = s[l:r+1]
                    res = r - l + 1
                r += 1
                l -= 1
            
            l, r = i, i + 1
            while l >= 0 and r < L and s[l] == s[r]:
                if r - l + 1 > res:
                    string = s[l:r+1]
                    res = r - l + 1
                r += 1
                l -= 1
        
        return string

        