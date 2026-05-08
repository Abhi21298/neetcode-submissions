class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        maps = {"+" : lambda x,y : x + y,
                "-" : lambda x,y : y - x,
                "*" : lambda x,y : x * y,
                "/" : lambda x,y : int(y / x)}

        stack = []

        for ch in tokens:

            if ch in maps and len(stack) >= 2:
                res = maps[ch](int(stack.pop()), int(stack.pop()))

                stack.append(res)
            else:
                stack.append(int(ch))
        
        return stack[0]
        