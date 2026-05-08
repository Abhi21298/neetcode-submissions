class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []
        
        intervals.sort(key = lambda x : x[0])
        last = intervals[0]
        output = [last]
        
        for start, end in intervals[1:]:
            if start <= last[1]:
                last[1] = max(end, last[1])
            else:
                output.append([start, end])
                last = output[-1]
        
        return output

        