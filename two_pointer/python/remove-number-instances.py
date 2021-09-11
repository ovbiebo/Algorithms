def remove_duplicates(arr, key):
    left = right = 0
    while right < len(arr):
        arr[left] = arr[right]
        if arr[left] != key:
            left += 1
        right += 1

    return left


if __name__ == '__main__':
    print(remove_duplicates([3, 2, 3, 6, 3, 10, 9, 3], 3))
    print(remove_duplicates([2, 11, 2, 2, 1], 2))
