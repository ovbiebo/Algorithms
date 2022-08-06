from heapq import *


def find_Kth_smallest(lists, k):
    number = -1
    min_heap = []
    for num_list in lists:
        heappush(min_heap, (num_list[0], 1, num_list))

    count = 0
    while count < k and min_heap:
        num, next_index, num_list = heappop(min_heap)
        if next_index < len(num_list):
            heappush(min_heap, (num_list[next_index], next_index + 1, num_list))
        number = num
        count += 1

    return -1 if count < k else number


if __name__ == "__main__":
    print("Kth smallest number is: " + str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
    print("Kth smallest number is: " + str(find_Kth_smallest([[5, 8, 9], [1, 7]], 3)))
