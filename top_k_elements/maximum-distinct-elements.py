from heapq import *


def find_maximum_distinct_elements(nums, k):
    result = 0
    if len(nums) <= k:
        return result

    frequency_map = {}
    min_heap = []

    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    for num, frequency in frequency_map.items():
        if frequency == 1:
            result += 1
        else:
            heappush(min_heap, (frequency, num))

    while min_heap and k > 0:
        k -= heappop(min_heap)[0] - 1
        if k >= 0:
            result += 1

    return result - max(k, 0)


if __name__ == '__main__':
    print(f"Maximum distinct numbers after removing K numbers: "
          f"{find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)}")  # 3
    print(f"Maximum distinct numbers after removing K numbers: "
          f"{find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)}")  # 2
    print(f"Maximum distinct numbers after removing K numbers: "
          f"{find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)}")  # 3
