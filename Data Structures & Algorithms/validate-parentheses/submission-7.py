class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        track = {')' : '(', '}' : '{', ']': '['}

        for ch in s:
            if ch in track:
                if not stack or track[ch] != stack[-1]:
                    return False
                stack.pop(-1)
            else:
                stack.append(ch)

        return True if not stack else False