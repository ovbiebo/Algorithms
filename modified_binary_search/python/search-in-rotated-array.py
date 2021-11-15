def search_ratated_array(arr, key):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[start]:
            start = mid
        else:
            end = mid

    result = binary_search(arr, key, 0, end)
    if result == -1:
        result = binary_search(arr, key, start + 1, len(arr) - 1)

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
    print(search_ratated_array([10, 15, 1, 3, 8], 15))
    print(search_ratated_array([4, 5, 7, 9, 10, -1, 2], 10))
