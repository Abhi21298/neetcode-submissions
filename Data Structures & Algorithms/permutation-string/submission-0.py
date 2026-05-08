class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False


        ct1 = {}
        ct2 = {}

        for i in range(len(s1)):
            ct1[s1[i]] = ct1.get(s1[i], 0) + 1
            ct2[s2[i]] = ct2.get(s2[i], 0) + 1
        
        if ct1 == ct2:
            return True
            # return s2[0:len(s1)]
            
        l = 0
        for r in range(len(s1), len(s2)):
            ct2[s2[r]] = ct2.get(s2[r], 0) + 1

            ct2[s2[l]] -= 1
            if ct2[s2[l]] == 0:
                del ct2[s2[l]]
            l += 1

            if ct1 == ct2:
                return True
                # return s2[l: r + 1]
        
        return False
        