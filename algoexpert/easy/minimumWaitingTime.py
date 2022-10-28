# O(nlog(n)) time | O(1) space
def minimumWaitingTime(queries):
    queries.sort()

    running_wait_time = 0
    total_wait_time = 0

    for idx in range(0, len(queries) - 1):
        running_wait_time += queries[idx]
        total_wait_time += running_wait_time

    return total_wait_time
