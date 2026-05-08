class Solution:
    def isValid(self, s: str) -> bool:

        track = {']': '[', '}': '{', ')': '('}
        stack = []

        for c in s:
            if c in track.keys():
                if stack and track[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

        