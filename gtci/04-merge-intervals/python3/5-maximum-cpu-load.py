import heapq


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpuLoad = cpu_load


class Solution:
    def findMaxCPULoad(self, jobs):
        if len(jobs) < 2:
            return 0 if len(jobs) == 0 else jobs[0].cpuLoad

        jobs.sort(key=lambda x: x.start)

        max_cpu_load = 0

        current_cpu_load = 0
        min_heap = []

        for job in jobs:
            while min_heap and min_heap[0][1] <= job.start:
                popped_job = heapq.heappop(min_heap)
                current_cpu_load -= popped_job[2]

            heapq.heappush(min_heap, (job.start, job.end, job.cpuLoad))
            current_cpu_load += job.cpuLoad

            max_cpu_load = max(max_cpu_load, current_cpu_load)

        return max_cpu_load


if __name__ == "__main__":
    sol = Solution()

    assert sol.findMaxCPULoad([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)]) == 7
    assert sol.findMaxCPULoad([Job(6, 7, 2), Job(2, 4, 11), Job(8, 12, 15)]) == 15
    assert sol.findMaxCPULoad([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)]) == 8

    print("All test cases passed.")
