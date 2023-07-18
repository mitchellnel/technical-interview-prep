from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    max_start_heap = []
    max_end_heap = []

    next_intervals = [-1 for _ in range(len(intervals))]

    # put all the intervals in the heaps
    for idx, interval in enumerate(intervals):
        heappush(max_start_heap, (-interval.start, idx))
        heappush(max_end_heap, (-interval.end, idx))

    # go through all of the intervals to find each interval's next interval
    for _ in range(len(intervals)):
        # find the next interval of the interval that currently has the largest
        #   end time
        top_end, top_end_idx = heappop(max_end_heap)

        print(f"top_end: {top_end}")

        if -max_start_heap[0][0] >= -top_end:
            top_start, top_start_idx = heappop(max_start_heap)

            print(f"top_start: {top_start}")

            # find the interval that has the closest start
            while len(max_start_heap) > 0 and -max_start_heap[0][0] >= -top_end:
                top_start, top_start_idx = heappop(max_start_heap)

            next_intervals[top_end_idx] = top_start_idx

            # put the interval back as it could be the next interval of other
            #   intervals
            heappush(max_start_heap, (top_start, top_start_idx))

    return next_intervals


def main():
    result = find_next_interval([Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval([Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


main()
