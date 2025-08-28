class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end=" ")


def insertInterval(intervals, new_interval):
    merged = []

    i = 0
    # skip (and add to output) all intervals that come before the new interval
    while i < len(intervals) and intervals[i].end < new_interval.start:
        merged.append(intervals[i])

        i += 1

    # i is now the first interval that overlaps with new_interval
    # merge all intervals that overlap with new_interval
    while i < len(intervals) and intervals[i].start <= new_interval.end:
        new_interval.start = min(intervals[i].start, new_interval.start)
        new_interval.end = max(intervals[i].end, new_interval.end)

        i += 1

    # insert the new interval
    merged.append(new_interval)

    # add all of the remaining intervals to the output
    while i < len(intervals):
        merged.append(intervals[i])

        i += 1

    return merged


def main():
    print("Intervals after inserting the new interval: ")
    for interval in insertInterval(
        [Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 6)
    ):
        interval.print_interval()
    print()

    print("Intervals after inserting the new interval: ")
    for interval in insertInterval(
        [Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 10)
    ):
        interval.print_interval()
    print()

    print("Intervals after inserting the new interval: ")
    for interval in insertInterval([Interval(2, 3), Interval(5, 7)], Interval(1, 4)):
        interval.print_interval()
    print()


main()
