def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    is_ascending = arr[start] < arr[end]

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return mid

        if is_ascending:
            if arr[mid] < key:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if arr[mid] > key:
                start = mid + 1
            else:
                end = mid - 1

    return -1


if __name__ == '__main__':
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))
