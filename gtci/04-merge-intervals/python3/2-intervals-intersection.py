class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def merge(self, intervals_a, intervals_b):
        result = []

        i = 0
        j = 0

        while i < len(intervals_a) and j < len(intervals_b):
            start = max(intervals_a[i].start, intervals_b[j].start)
            end = min(intervals_a[i].end, intervals_b[j].end)

            if start <= end:
                result.append([start, end])

            if intervals_a[i].end < intervals_b[j].end:
                i += 1
            else:
                j += 1

        return result


if __name__ == "__main__":
    from util import assert_equal_interval

    sol = Solution()

    assert sol.merge(
        [Interval(1, 3), Interval(5, 6), Interval(7, 9)],
        [Interval(2, 3), Interval(5, 7)],
    ) == [[2, 3], [5, 6], [7, 7]]

    assert sol.merge(
        [Interval(1, 3), Interval(5, 7), Interval(9, 12)],
        [Interval(5, 10)],
    ) == [[5, 7], [9, 10]]

    print("All test cases passed.")
