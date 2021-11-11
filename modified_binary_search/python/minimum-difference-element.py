def search_min_diff_element(arr, key):
    start, end = 0, len(arr) - 1
    min_diff = arr[0]

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] < key:
            if (key - arr[mid]) < (key - min_diff):
                min_diff = arr[mid]
            start = mid + 1
        else:
            if (arr[mid] - key) < (min_diff - key):
                min_diff = arr[mid]
            end = mid - 1

    return min_diff


if __name__ == '__main__':
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))
