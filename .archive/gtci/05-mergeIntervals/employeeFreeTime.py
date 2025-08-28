import heapq


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end=" ")


class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours

        # index of the list containing working hours of this employee
        self.employee_index = employeeIndex
        self.interval_index = (
            intervalIndex  # index of the interval in the employee list
        )

    def __lt__(self, other):
        # min heap based on meeting.start
        return self.interval.start < other.interval.start


def employeeFreeTime(schedule):
    if schedule is None:
        return []

    result = []
    min_heap = []

    # insert the first interval of each employee to the min heap
    for i in range(len(schedule)):
        heapq.heappush(min_heap, EmployeeInterval(schedule[i][0], i, 0))

    prev_interval = min_heap[0].interval
    while len(min_heap) > 0:
        heap_top = heapq.heappop(min_heap)
        curr_interval = heap_top.interval

        # if prev_interval is not overlapping with the next interval,
        #   insert a free interval
        if prev_interval.end < curr_interval.start:
            result.append(Interval(prev_interval.end, curr_interval.start))

            prev_interval = curr_interval
        else:
            # overlapping intervals
            # update prev_interval if needed
            if prev_interval.end < curr_interval.end:
                prev_interval = curr_interval

        # if there are more intervals for the same employee, add their next interval
        employee_schedule = schedule[heap_top.employee_index]
        if len(employee_schedule) > heap_top.interval_index + 1:
            heapq.heappush(
                min_heap,
                EmployeeInterval(
                    employee_schedule[heap_top.interval_index + 1],
                    heap_top.employee_index,
                    heap_top.interval_index + 1,
                ),
            )

    return result


def main():
    input = [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end="")
    for interval in employeeFreeTime(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end="")
    for interval in employeeFreeTime(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end="")
    for interval in employeeFreeTime(input):
        interval.print_interval()
    print()


main()
