from heapq import *


def find_k_frequent_numbers(nums, k):
    top_numbers = []
    top_numbers_heap = []
    frequencies = {}

    for num in nums:
        frequencies[num] = frequencies.get(num, 0) + 1

    for num, frequency in frequencies.items():
        if len(top_numbers_heap) < k or frequency > frequencies[top_numbers_heap[0][1]]:
            heappush(top_numbers_heap, (frequency, num))
        if len(top_numbers_heap) > k:
            heappop(top_numbers_heap)

    while top_numbers_heap:
        top_numbers.append(heappop(top_numbers_heap)[1])

    return top_numbers


if __name__ == '__main__':
    print(f"here are the K frequent numbers: "
          f"{find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)}")  # [12, 11]
    print(f"here are the K frequent numbers: "
          f"{find_k_frequent_numbers([5, 12, 11, 3, 11], 2)}")  # [11, 5] or [11, 12] or [11, 3]
