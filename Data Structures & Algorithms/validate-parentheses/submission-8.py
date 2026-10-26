class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s:
            return True
        
        maps = {'}': '{', ']' : '[', ')' : '('}
        stack = []

        for i in range(len(s)):

            if s[i] in maps.keys():

                if not stack or stack[-1] != maps[s[i]]:
                    return False
                stack.pop(-1)
                continue
                
            stack.append(s[i])
        
        return True if len(stack) == 0 else False
