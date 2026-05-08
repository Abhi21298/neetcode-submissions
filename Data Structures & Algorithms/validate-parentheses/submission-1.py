class Solution:
    def isValid(self, s: str) -> bool:

        if s == '':
            return True

        pairs = {')':'(',\
                '}':'{',\
                ']':'['}
        
        stack = []
        for i in s:
            if i in pairs:
                if stack and stack[0] == pairs[i]:
                    stack.pop(0)
                else:
                    return False
            else:
                stack.insert(0, i)
        
        return True if not stack else False





        