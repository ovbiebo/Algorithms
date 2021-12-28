from heapq import *


def find_k_largest_numbers(nums, k):
    result = []
    for num in nums:
        if len(result) < k - 1 or num > result[0]:
            heappush(result, num)
        if len(result) > k:
            heappop(result)

    return result


if __name__ == '__main__':
    print(f"Here are the top K numbers {find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)}")  # [5, 12, 11]
    print(f"Here are the top K numbers {find_k_largest_numbers([5, 12, 11, -1, 12], 3)}")  # [12, 11, 12]
