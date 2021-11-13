def search_bitonic_array(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return arr[start]


if __name__ == '__main__':
    print(search_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(search_bitonic_array([3, 8, 3, 1]))
    print(search_bitonic_array([1, 3, 8, 12]))
    print(search_bitonic_array([10, 9, 8]))
