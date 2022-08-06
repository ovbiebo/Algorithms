from heapq import *


def find_smallest_range(lists):
    range_start, range_end = -1, -1
    min_heap = []
    for num_list in lists:
        range_end = max(range_end, num_list[0])
        heappush(min_heap, (num_list[0], 1, num_list))

    smallest_range = []
    while len(min_heap) == len(lists):
        range_start, next_index, num_list = heappop(min_heap)
        if not smallest_range or smallest_range[1] - smallest_range[0] > range_end - range_start:
            smallest_range = [range_start, range_end]
        if next_index < len(num_list):
            range_end = max(range_end, num_list[next_index])
            heappush(min_heap, (num_list[next_index], next_index + 1, num_list))

    return smallest_range if smallest_range else [-1, -1]


if __name__ == "__main__":
    print("Smallest range is: " + str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))
    print("Smallest range is: " + str(find_smallest_range([[1, 9], [4, 12], [7, 10, 16]])))
