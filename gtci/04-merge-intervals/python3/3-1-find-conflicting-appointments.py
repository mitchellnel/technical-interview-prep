import heapq


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f"[{self.start}, {self.end}]"

    def __repr__(self):
        return f"Interval({self.start}, {self.end})"


class Solution:
    def getConflictingAppointments(self, intervals):
        if len(intervals) < 2:
            return []

        heap = []
        conflicts = []

        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            # pop all intervals that end before the current one starts
            while heap and heap[0][0] <= interval.start:
                heapq.heappop(heap)

            # all remaining intervals in the heap conflict with the current interval
            for conflict in heap:
                conflicts.append(
                    [
                        [conflict[1].start, conflict[1].end],
                        [interval.start, interval.end],
                    ]
                )

            # push the current interval onto the heap
            heapq.heappush(heap, (interval.end, interval))

        return conflicts


if __name__ == "__main__":
    sol = Solution()

    assert sol.getConflictingAppointments(
        [Interval(4, 5), Interval(2, 3), Interval(3, 6), Interval(5, 7), Interval(7, 8)]
    ) == [[[3, 6], [4, 5]], [[3, 6], [5, 7]]]

    print("All test cases passed.")
