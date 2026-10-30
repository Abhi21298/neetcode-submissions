"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = []
        end = []

        for x in intervals:
            start.append(x.start)
            end.append(x.end)
        
        start.sort()
        end.sort()

        res, count = 0, 0
        s, e = 0, 0

        while s < len(start):

            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            
            res = max(res, count)
        
        return res


        