def remove_duplicates(arr):
    left = right = 1
    while right < len(arr):
        arr[left] = arr[right]
        if arr[left] != arr[left - 1]:
            left += 1
        right += 1

    return left


if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
