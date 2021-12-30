from heapq import *


def find_sum_of_elements(nums, k1, k2):
    result = 0
    if k1 < 0 or k2 < k1:
        return result

    max_heap = []
    for num in nums:
        if len(max_heap) < k2 - 1 or num < -max_heap[0]:
            heappush(max_heap, -num)
        if len(max_heap) > k2 - 1:
            heappop(max_heap)

    for i in range(len(max_heap) - k1):
        result -= heappop(max_heap)

    return result


if __name__ == '__main__':
    print(f"Sum of all numbers between k1 and k2 smallest numbers: "
          f"{find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)}")  # 23
    print(f"Sum of all numbers between k1 and k2 smallest numbers: "
          f"{find_sum_of_elements([3, 5, 8, 7], 1, 4)}")  # 12
