def count_rotations(arr):
    start, end = 0, len(arr) - 1

    if arr[end] > arr[start]:
        return 0

    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[start]:
            start = mid
        else:
            end = mid

    return start + 1

if __name__ == '__main__':
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))
