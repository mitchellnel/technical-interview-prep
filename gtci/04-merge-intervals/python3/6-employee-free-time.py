import heapq


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class EmployeeInterval:

    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex  # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start

    def __str__(self):
        return f"({self.employeeIndex}: ({self.intervalIndex}, {self.interval}))"

    def __repr__(self):
        return self.__str__()


class Solution:
    def findEmployeeFreeTime(self, schedule):
        result = []

        min_heap = []

        for idx, employee_schedule in enumerate(schedule):
            heapq.heappush(min_heap, EmployeeInterval(employee_schedule[0], idx, 0))

        previous_interval = min_heap[0].interval

        while min_heap:
            top = heapq.heappop(min_heap)
            earliest_start_interval = top.interval

            if previous_interval.end < earliest_start_interval.start:
                result.append([previous_interval.end, earliest_start_interval.start])
                previous_interval = earliest_start_interval
            else:
                previous_interval.start = min(
                    previous_interval.start, earliest_start_interval.start
                )
                previous_interval.end = max(
                    previous_interval.end, earliest_start_interval.end
                )

            # add more of the employee's intervals if they have any
            if top.intervalIndex + 1 < len(schedule[top.employeeIndex]):
                heapq.heappush(
                    min_heap,
                    EmployeeInterval(
                        schedule[top.employeeIndex][top.intervalIndex + 1],
                        top.employeeIndex,
                        top.intervalIndex + 1,
                    ),
                )

        return result


if __name__ == "__main__":
    sol = Solution()

    assert sol.findEmployeeFreeTime(
        [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
    ) == [[3, 5]]

    assert sol.findEmployeeFreeTime(
        [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4), Interval(6, 8)]]
    ) == [[4, 6], [8, 9]]

    assert sol.findEmployeeFreeTime(
        [[Interval(1, 3), Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    ) == [[5, 7]]

    print("All test cases passed.")
