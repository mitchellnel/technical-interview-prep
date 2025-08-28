class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end=" ")


def mergeIntervals(intervals):
    if len(intervals) < 2:
        return intervals

    # sort the intervals based on the start time
    intervals.sort(key=lambda x: x.start)

    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):
        curr_interval = intervals[i]

        if curr_interval.start <= end:
            # overlapping intervals -- adjust the end
            end = max(curr_interval.end, end)
        else:
            # non-overlapping interval -- add the previous interval and reset
            merged_intervals.append(Interval(start, end))

            start = curr_interval.start
            end = curr_interval.end

    # add the last interval
    merged_intervals.append(Interval(start, end))

    return merged_intervals


def main():
    print("Merged intervals: ", end="")
    for i in mergeIntervals([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end="")
    for i in mergeIntervals([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end="")
    for i in mergeIntervals([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
