import heapq
from heapq import *


class SlidingWindowMedian:
    def __init__(self):
        # remember to flip sign of any numbers going into the max_heap so that
        #   it works like a max_heap
        #   (and especially remember to flip the sign as we pop from the heap)
        self.max_heap = []
        self.min_heap = []

    def find_sliding_window_medians(self, nums, k):
        medians = [0.0 for _ in range(len(nums) - k + 1)]

        window_start = 0
        for window_end in range(len(nums)):
            print(medians)
            self.insert_num(nums[window_end])

            # if we have at least k elements in the sliding window, add the
            #   median to the medians array
            if window_end - window_start + 1 >= k:
                medians[window_end - k + 1] = self.find_median()

                # remove the element going out of the sliding window
                elem_to_remove = nums[window_start]
                if elem_to_remove <= -self.max_heap[0]:
                    self.remove_num(self.max_heap, -elem_to_remove)
                else:
                    self.remove_num(self.min_heap, elem_to_remove)

                window_start += 1

        return medians

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            # we have an even number of elements
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return float(-self.max_heap[0])

    def insert_num(self, num):
        if not len(self.max_heap) > 0 or num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # rebalance the heaps if necessary
        self.rebalance_heaps()

    def remove_num(self, heap, num):
        # find the element
        idx = heap.index(num)

        # copy the last element of the heap to this index, and then decrement
        #   the heap size
        heap[idx] = heap[-1]
        del heap[-1]

        # adjust the position of the element while maintaining the heap
        #   property
        # we could use `heapify`, but this would be O(n)
        # instead we will adjust only one element which is O(log n)
        if idx < len(heap):
            # move the element at idx up the heap to maintain heap order
            #   property
            heapq._siftup(heap, idx)

            # move around all the elements from 0 -- idx to maintain heap order
            #   property
            heapq._siftdown(heap, 0, idx)

        self.rebalance_heaps()

    def rebalance_heaps(self):
        # either both heaps will have the same number of elements,
        #   or max_heap will have 1 more element than min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))


def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_medians([1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_medians([1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
