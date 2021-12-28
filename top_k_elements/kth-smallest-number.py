from heapq import *


def find_k_smallest_numbers(nums, k):
    result = []
    for num in nums:
        if len(result) < k - 1 or num < -result[0]:
            heappush(result, -num)
        if len(result) > k:
            heappop(result)

    return -result[0]


if __name__ == '__main__':
    print(f"Kth smallest number is: {find_k_smallest_numbers([1, 5, 12, 2, 11, 5], 3)}")  # 5
    print(f"Kth smallest number is: {find_k_smallest_numbers([1, 5, 12, 2, 11, 5], 4)}")  # 5
    print(f"Kth smallest number is: {find_k_smallest_numbers([5, 12, 11, -1, 12], 3)}")  # 11
