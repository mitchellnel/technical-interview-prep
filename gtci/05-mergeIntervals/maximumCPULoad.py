import heapq


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        # min heap based on Job.end
        return self.end < other.end


def maximumCPULoad(jobs):
    # sort the Jobs based on their start time
    jobs.sort(key=lambda x: x.start)

    max_load = 0
    curr_load = 0
    min_heap = []
    for job in jobs:
        # remove all the Jobs that have ended
        while len(min_heap) > 0 and job.start >= min_heap[0].end:
            curr_load -= min_heap[0].cpu_load
            heapq.heappop(min_heap)

        # add the current Job to the min heap
        heapq.heappush(min_heap, job)
        curr_load += job.cpu_load

        # if it is a new max, store it
        max_load = max(max_load, curr_load)

    return max_load


def main():
    print(
        "Maximum CPU load at any time: "
        + str(maximumCPULoad([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)]))
    )
    print(
        "Maximum CPU load at any time: "
        + str(maximumCPULoad([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)]))
    )
    print(
        "Maximum CPU load at any time: "
        + str(maximumCPULoad([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)]))
    )


main()
