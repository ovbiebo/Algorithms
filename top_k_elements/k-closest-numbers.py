from heapq import *


def find_closest_elements(arr, K, X):
    result = []
    maxHeap = []
    for num in arr:
        diff = (X - num)**2
        if len(maxHeap) < K or diff < -maxHeap[0][0]:
            heappush(maxHeap, (-diff, num))
        if len(maxHeap) > K:
            heappop(maxHeap)

    for _ in range(K):
        result.append(heappop(maxHeap)[1])

    return sorted(result)


if __name__ == '__main__':
    print(f"'K' closest numbers to 'X' are: {find_closest_elements([5, 6, 7, 8, 9], 3, 7)}")  # [6, 7, 8]
    print(f"'K' closest numbers to 'X' are: {find_closest_elements([2, 4, 5, 6, 9], 3, 6)}")  # [4, 5, 6]
    print(f"'K' closest numbers to 'X' are: {find_closest_elements([2, 4, 5, 6, 9], 3, 10)}")  # [5, 6, 9]
