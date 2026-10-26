class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]*len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                i = stack.pop()
                result[i] = idx - i

            stack.append(idx)
        
        return result