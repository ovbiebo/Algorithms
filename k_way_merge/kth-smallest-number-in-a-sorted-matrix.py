from heapq import *


def find_Kth_smallest(matrix, k):
    number = -1
    min_heap = []
    for row in matrix:
        heappush(min_heap, (row[0], 1, row))

    count = 0
    while count < k and min_heap:
        num, next_index, num_list = heappop(min_heap)
        if next_index < len(num_list):
            heappush(min_heap, (num_list[next_index], next_index + 1, num_list))
        number = num
        count += 1

    return -1 if count < k else number


if __name__ == "__main__":
    print("Kth smallest number is: " + str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))
