# O(nlog(n)) time | O(n) space
def mergeOverlappingIntervals(intervals):
    merged = []

    intervals.sort()

    for i in range(0, len(intervals)):
        if merged and merged[-1][1] >= intervals[i][0]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])

    return merged
