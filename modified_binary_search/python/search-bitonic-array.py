def search_bitonic_array(arr, key):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    result = binary_search(arr, key, 0, end)
    if result == -1:
        result = binary_search(arr, key, start, len(arr) - 1)

    return result


def binary_search(arr, key, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


if __name__ == '__main__':
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))
