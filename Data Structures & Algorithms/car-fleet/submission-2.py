class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        track = list()
        for pos, sp in zip(position, speed):
            track.append([pos, sp])
        
        track.sort(key = lambda x: x[0], reverse = True)
        stack = []
        
        for pos, sp in track:

            time = (target - pos) / sp
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        
        return len(stack)


