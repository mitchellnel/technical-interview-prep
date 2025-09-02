class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"

    def __repr__(self):
        return self.__str__()


class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        merged_intervals = []

        intervals.sort(key=lambda x: x.start)

        start = intervals[0].start
        end = intervals[0].end
        for i in range(1, len(intervals)):
            interval = intervals[i]

            if interval.start <= end:
                end = max(end, interval.end)
            else:
                merged_intervals.append(Interval(start, end))

                start = interval.start
                end = interval.end

        merged_intervals.append(Interval(start, end))

        return merged_intervals


if __name__ == "__main__":
    from util import assert_equal_interval

    sol = Solution()

    # Test case 1: Overlapping intervals
    result1 = sol.merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)])
    assert_equal_interval(result1[0], Interval(1, 5))
    assert_equal_interval(result1[1], Interval(7, 9))
    assert len(result1) == 2

    # Test case 2: Non-overlapping and overlapping intervals
    result2 = sol.merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)])
    assert_equal_interval(result2[0], Interval(2, 4))
    assert_equal_interval(result2[1], Interval(5, 9))
    assert len(result2) == 2

    # Test case 3: All intervals merge into one
    result3 = sol.merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)])
    assert_equal_interval(result3[0], Interval(1, 6))
    assert len(result3) == 1

    print("All test cases passed.")
