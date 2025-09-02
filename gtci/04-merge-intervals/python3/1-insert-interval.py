class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def insert(self, intervals, new_interval):
        merged = []

        idx = 0

        # find and add all intervals ending before the new interval
        while idx < len(intervals) and intervals[idx].end < new_interval.start:
            merged.append(intervals[idx])
            idx += 1

        # deal with all intervals overlapping with the new interval
        while idx < len(intervals) and intervals[idx].start <= new_interval.end:
            new_interval.start = min(new_interval.start, intervals[idx].start)
            new_interval.end = max(new_interval.end, intervals[idx].end)

            idx += 1

        merged.append(new_interval)

        # now add the remaining intervals
        while idx < len(intervals):
            merged.append(intervals[idx])
            idx += 1

        return merged


if __name__ == "__main__":
    from util import assert_equal_interval

    sol = Solution()

    result1 = sol.insert(
        [Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 6)
    )
    assert_equal_interval(result1[0], Interval(1, 3))
    assert_equal_interval(result1[1], Interval(4, 7))
    assert_equal_interval(result1[2], Interval(8, 12))
    assert len(result1) == 3

    result2 = sol.insert(
        [Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 10)
    )
    assert_equal_interval(result2[0], Interval(1, 3))
    assert_equal_interval(result2[1], Interval(4, 12))
    assert len(result2) == 2

    result3 = sol.insert([Interval(2, 3), Interval(5, 7)], Interval(1, 4))
    assert_equal_interval(result3[0], Interval(1, 4))
    assert_equal_interval(result3[1], Interval(5, 7))
    assert len(result3) == 2

    print("All test cases passed.")
