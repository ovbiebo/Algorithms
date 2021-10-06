from heapq import *


class MedianOfAStream:
    max_heap = []
    min_heap = []

    def insert_num(self, num):
        if not self.max_heap or num < -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) - len(self.min_heap) > 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0])/2


if __name__ == '__main__':
    median_of_a_stream = MedianOfAStream()
    median_of_a_stream.insert_num(3)
    median_of_a_stream.insert_num(1)
    print(f"The median is: {median_of_a_stream.find_median()}")
    median_of_a_stream.insert_num(5)
    print(f"The median is: {median_of_a_stream.find_median()}")
    median_of_a_stream.insert_num(4)
    print(f"The median is: {median_of_a_stream.find_median()}")
