class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for i in range(len(asteroids)):
            
            stack.append(asteroids[i])

            while len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0:

                coll = stack[-1] + stack[-2]
                if coll == 0:
                    stack.pop()
                    stack.pop()
                elif abs(stack[-1]) > stack[-2]:
                    val = stack.pop()
                    stack[-1] = val
                else:
                    stack.pop()

        
        return stack
