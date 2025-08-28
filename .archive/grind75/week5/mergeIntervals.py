from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []

        intervals.sort()

        for interval in intervals:
            if len(merged_intervals) > 0 and interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
            else:
                merged_intervals.append(interval)

        return merged_intervals


def main():
    soln = Solution()

    print(
        f"[[1,3],[2,6],[8,10],[15,18]] --> {soln.merge([[1,3],[2,6],[8,10],[15,18]])}"
    )
    print(f"[[1,4],[4,5]] --> {soln.merge([[1,4],[4,5]])}")


main()
