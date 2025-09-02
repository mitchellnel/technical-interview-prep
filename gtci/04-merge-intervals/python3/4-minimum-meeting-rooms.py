import heapq


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start < other.start


class Solution:
    def findMinimumMeetingRooms(self, meetings):
        if len(meetings) < 1:
            return len(meetings)

        min_heap = []
        min_rooms = 0

        meetings.sort(key=lambda x: x.start)

        for meeting in meetings:
            while len(min_heap) > 0 and min_heap[0][1].end <= meeting.start:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, (meeting.end, meeting))

            min_rooms = max(min_rooms, len(min_heap))

        return min_rooms


if __name__ == "__main__":
    sol = Solution()

    assert (
        sol.findMinimumMeetingRooms([Interval(1, 4), Interval(2, 5), Interval(7, 9)])
        == 2
    )
    assert (
        sol.findMinimumMeetingRooms([Interval(6, 7), Interval(2, 4), Interval(8, 12)])
        == 1
    )
    assert (
        sol.findMinimumMeetingRooms([Interval(1, 4), Interval(2, 3), Interval(3, 6)])
        == 2
    )
    assert (
        sol.findMinimumMeetingRooms(
            [Interval(4, 5), Interval(2, 3), Interval(2, 4), Interval(3, 5)]
        )
        == 2
    )

    print("All test cases passed.")
