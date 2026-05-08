class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for item in asteroids:
            while stack and stack[-1] > 0 and item < 0:
                diff = stack[-1] + item
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    item = 0
                else:
                    item = 0
                    stack.pop()
            
            if item:
                stack.append(item)
        
        return stack
        