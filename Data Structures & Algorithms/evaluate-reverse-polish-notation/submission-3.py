class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        maps = {"+": lambda x,y: x + y, 
                "-": lambda x,y: y - x, 
                "*": lambda x,y: x * y, 
                "/": lambda x,y: int(y / x)}
        
        stack = []
        for i in tokens:
            if i in maps and stack:
                res = maps[i](int(stack.pop()), int(stack.pop()))
                stack.append(res)
            else:
                stack.append(int(i))
        
        return stack[0]

            
        