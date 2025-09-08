import heapq


class Solution:

    def __init__(self):
        self.smaller_half_max_heap = []
        self.larger_half_min_heap = []
        self.median = None

    def insertNum(self, num):
        if not self.smaller_half_max_heap or (
            self.median is not None and num <= self.median
        ):
            heapq.heappush(self.smaller_half_max_heap, -num)
        else:
            heapq.heappush(self.larger_half_min_heap, num)

        self.rebalance_heaps()
        self.recalculate_median()

    def findMedian(self):
        return self.median

    def rebalance_heaps(self):
        if len(self.smaller_half_max_heap) > len(self.larger_half_min_heap) + 1:
            popped_num = -heapq.heappop(self.smaller_half_max_heap)
            heapq.heappush(self.larger_half_min_heap, popped_num)
        elif len(self.smaller_half_max_heap) + 1 < len(self.larger_half_min_heap):
            popped_num = heapq.heappop(self.larger_half_min_heap)
            heapq.heappush(self.smaller_half_max_heap, -popped_num)

    def recalculate_median(self):
        if len(self.smaller_half_max_heap) > len(self.larger_half_min_heap):
            self.median = float(-self.smaller_half_max_heap[0])
        elif len(self.smaller_half_max_heap) < len(self.larger_half_min_heap):
            self.median = float(self.larger_half_min_heap[0])
        else:
            self.median = (
                -self.smaller_half_max_heap[0] + self.larger_half_min_heap[0]
            ) / 2


if __name__ == "__main__":
    sol = Solution()
    sol.insertNum(3)
    sol.insertNum(1)
    assert sol.findMedian() == 2.0
    sol.insertNum(5)
    assert sol.findMedian() == 3.0
    sol.insertNum(4)
    assert sol.findMedian() == 3.5

    print("All test cases passed.")
