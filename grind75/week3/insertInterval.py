from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]

        left = []
        right = []
        for interval in intervals:
            # case 1: interval[1] < new_start
            #   no need to merge, just add to our array
            if interval[1] < new_start:
                left.append(interval)
            # case 2: interval[0] > new_end
            #   no need to merge, just add to our array
            elif interval[0] > new_end:
                right.append(interval)
            # case 3: there exists some overlap between interval and newInterval
            #   work out how to merge
            else:
                new_start = min(new_start, interval[0])
                new_end = max(new_end, interval[1])

        # merge the intervals less than newInterval, the newInterval, and the
        #   intervals greater than newInterval
        merged = left + [[new_start, new_end]] + right
        return merged


def main():
    soln = Solution()

    print(f"Insert [2,5] into [[1,3],[6,9]]: {soln.insert([[1,3],[6,9]], [2,5])}")
    print(
        f"Insert [4,8] into [[1,2],[3,5],[6,7],[8,10],[12,16]]: {soln.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])}"
    )


main()
