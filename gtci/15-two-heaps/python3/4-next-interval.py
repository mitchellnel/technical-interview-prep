import heapq


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def findNextInterval(self, intervals):
        result = [-1 for x in range(len(intervals))]

        start_max_heap = []
        end_max_heap = []

        for i in range(len(intervals)):
            heapq.heappush(start_max_heap, (-intervals[i].start, i))
            heapq.heappush(end_max_heap, (-intervals[i].end, i))

        while end_max_heap:
            # pop the end max heap
            end, curr_interval_idx = heapq.heappop(end_max_heap)
            end = -end

            # the last interval to be popped will be the next interval
            start, next_interval_idx = -1, -1
            while start_max_heap and -start_max_heap[0][0] >= end:
                start, next_interval_idx = heapq.heappop(start_max_heap)

            result[curr_interval_idx] = next_interval_idx

            if next_interval_idx != -1:
                # we process ends in descending order, so we don't need to put back the
                # start times we already popped

                # push back the last popped start time
                heapq.heappush(start_max_heap, (start, next_interval_idx))

        return result


if __name__ == "__main__":
    solution = Solution()

    intervals = [Interval(2, 3), Interval(3, 4), Interval(5, 6)]
    assert solution.findNextInterval(intervals) == [1, 2, -1]

    intervals = [Interval(3, 4), Interval(1, 5), Interval(4, 6)]
    assert solution.findNextInterval(intervals) == [2, -1, -1]

    print("All test cases passed.")
