class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendAllAppointments(self, intervals):
        if len(intervals) < 2:
            return True

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            first = intervals[i - 1]
            second = intervals[i]

            if second.start < first.end:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()

    assert not sol.canAttendAllAppointments(
        [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    )
    assert sol.canAttendAllAppointments(
        [
            Interval(6, 7),
            Interval(2, 4),
            Interval(13, 14),
            Interval(8, 12),
            Interval(45, 47),
        ]
    )
    assert not sol.canAttendAllAppointments(
        [Interval(4, 5), Interval(2, 3), Interval(3, 6)]
    )

    print("All test cases passed.")
