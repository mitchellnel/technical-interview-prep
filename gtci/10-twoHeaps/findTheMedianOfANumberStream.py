from heapq import *


class MedianOfAStream:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def insert_num(self, num):
        if not len(self.max_heap) > 0 or num <= -self.max_heap[0]:
            # use -num since we want it to work as a max_heap
            #   (just remember to use -self.max_heap[0] later to get the true value)
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # either both heaps will have the same number of elements,
        #   or max_heap will have 1 more element than min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

        print(self.max_heap, self.min_heap)

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            # we have an even number of elements
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return float(-self.max_heap[0])


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
