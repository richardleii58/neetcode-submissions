"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        meetings = []

        for interval in intervals:
            meetings.append([interval.start, interval.end])

        meetings.sort()

        prev = meetings[0]

        for i in range(1, len(meetings)):
            current = meetings[i]

            if current[0] < prev[1]:
                return False

            prev = current

        return True
