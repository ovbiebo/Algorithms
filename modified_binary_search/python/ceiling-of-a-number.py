def search_ceiling_of_a_number(arr, key):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            if start == end:
                return -1
            start = mid + 1
        else:
            if start == end:
                return mid
            end = mid - 1

    return 0


if __name__ == '__main__':
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))
