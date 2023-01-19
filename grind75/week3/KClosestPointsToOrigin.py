from math import sqrt, pow
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x1, x2, y1, y2):
            return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

        heap = []

        for point in points:
            x2, y2 = point
            distance = -dist(0, x2, 0, y2)

            if len(heap) == k:
                heapq.heappushpop(heap, (distance, x2, y2))
            else:
                heapq.heappush(heap, (distance, x2, y2))

        return [[x, y] for (dist, x, y) in heap]


def main():
    soln = Solution()

    print(f"points = [[1,3],[-2,2]]; k = 1 --> {soln.kClosest([[1,3],[-2,2]], 1)}")

    print(
        f"points = [[3,3],[5,-1],[-2,4]]; k = 2 --> {soln.kClosest([[3,3],[5,-1],[-2,4]], 2)}"
    )


main()
