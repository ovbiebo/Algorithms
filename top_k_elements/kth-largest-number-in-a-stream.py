from heapq import *


class KthLargestNumbersInStream:
    minHeap = []

    def __init__(self, nums, k):
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, num):
        if len(self.minHeap) < self.k or num > self.minHeap[0]:
            heappush(self.minHeap, num)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        if len(self.minHeap) < self.k:
            return None
        return self.minHeap[0]


if __name__ == '__main__':
    kthLargestNumber = KthLargestNumbersInStream([3, 1, 5, 12, 2, 11], 4)
    print(f"4th largest number is: {kthLargestNumber.add(6)}")  # 5
    print(f"4th largest number is: {kthLargestNumber.add(13)}")  # 6
    print(f"4th largest number is: {kthLargestNumber.add(4)}")  # 6
