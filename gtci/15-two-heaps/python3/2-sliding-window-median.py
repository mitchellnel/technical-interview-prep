import heapq
from collections import defaultdict


class Solution:
    def findSlidingWindowMedian(self, nums, k):
        medians = []

        median_finder = self.MedianFinder()

        window_start = 0
        for window_end in range(len(nums)):
            if window_end >= k:
                medians.append(median_finder.get_median())

                median_finder.delete_num(nums[window_start])
                window_start += 1

            median_finder.insert_num(nums[window_end])

        medians.append(median_finder.get_median())

        return medians

    class MedianFinder:
        def __init__(self):
            self.smaller_half_max_heap = []
            self.larger_half_min_heap = []

            self.lazy_deletions = defaultdict(int)

        def insert_num(self, num):
            if not self.smaller_half_max_heap or num <= -self.smaller_half_max_heap[0]:
                heapq.heappush(self.smaller_half_max_heap, -num)
            else:
                heapq.heappush(self.larger_half_min_heap, num)

            self.rebalance_heaps()

        def delete_num(self, num):
            self.lazy_deletions[num] += 1

            # clean tops if they've just been marked for deletion
            self.clean_top(self.smaller_half_max_heap, True)
            self.clean_top(self.larger_half_min_heap, False)
            self.rebalance_heaps()

        def get_median(self):
            self.clean_top(self.smaller_half_max_heap, True)
            self.clean_top(self.larger_half_min_heap, False)

            if len(self.smaller_half_max_heap) > len(self.larger_half_min_heap):
                return float(-self.smaller_half_max_heap[0])
            elif len(self.larger_half_min_heap) > len(self.smaller_half_max_heap):
                return float(self.larger_half_min_heap[0])
            else:
                return (
                    -self.smaller_half_max_heap[0] + self.larger_half_min_heap[0]
                ) / 2

        def rebalance_heaps(self):
            if len(self.smaller_half_max_heap) == len(self.larger_half_min_heap):
                return

            if len(self.smaller_half_max_heap) > len(self.larger_half_min_heap) + 1:
                heapq.heappush(
                    self.larger_half_min_heap,
                    -heapq.heappop(self.smaller_half_max_heap),
                )
            elif len(self.larger_half_min_heap) > len(self.smaller_half_max_heap) + 1:
                heapq.heappush(
                    self.smaller_half_max_heap,
                    -heapq.heappop(self.larger_half_min_heap),
                )

        def clean_top(self, heap, is_max_heap):
            while heap:
                num = -heap[0] if is_max_heap else heap[0]
                if self.lazy_deletions[num] > 0:
                    heapq.heappop(heap)
                    self.lazy_deletions[num] -= 1
                else:
                    break


if __name__ == "__main__":
    sol = Solution()
    assert sol.findSlidingWindowMedian([1, 2, -1, 3, 5], 2) == [1.5, 0.5, 1.0, 4.0]
    assert sol.findSlidingWindowMedian([1, 2, -1, 3, 5], 3) == [1.0, 2.0, 3.0]

    print("All test cases passed.")
