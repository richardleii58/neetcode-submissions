import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetings = []

        for interval in intervals:
            meetings.append([interval.start, interval.end])

        meetings.sort()

        heap = []

        for meeting in meetings:
            start = meeting[0]
            end = meeting[1]

            if len(heap) > 0 and heap[0] <= start:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

        return len(heap)