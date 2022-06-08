from heapq import *


class SlidingWindowMedian:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def find_sliding_window_median(self, nums, k):
        result = []
        for index, num in enumerate(nums):
            if not self.max_heap or num < -self.max_heap[0]:
                heappush(self.max_heap, -num)
            else:
                heappush(self.min_heap, num)

            self.balance()

            if len(self.max_heap) + len(self.min_heap) == k:
                median = -self.max_heap[0]
                if len(self.max_heap) == len(self.min_heap):
                    median = (-self.max_heap[0] + self.min_heap[0])/2
                result.append(median)

                num_to_drop = nums[index - k + 1]
                while self.max_heap and num_to_drop < -self.max_heap[0]:
                    heappush(self.min_heap, -heappop(self.max_heap))
                while self.min_heap and num_to_drop >= self.min_heap[0] and -self.max_heap[0] != self.min_heap[0]:
                    heappush(self.max_heap, -heappop(self.min_heap))
                heappop(self.max_heap)
                self.balance()

        return result

    def balance(self):
        while len(self.max_heap) - len(self.min_heap) > 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        while len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))


if __name__ == '__main__':
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))
