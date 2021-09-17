def dutch_flag_sort(arr):
    lz, ft = -1, len(arr)
    i = 0
    while i < ft:
        if arr[i] == 0 and i - lz > 1:
            lz += 1
            arr[i], arr[lz] = arr[lz], arr[i]
        elif arr[i] == 2 and ft - i > 1:
            ft -= 1
            arr[i], arr[ft] = arr[ft], arr[i]
        else:
            i += 1

    return arr


if __name__ == '__main__':
    print(dutch_flag_sort([1, 0, 2, 1, 0]))
    print(dutch_flag_sort([2, 2, 0, 1, 2, 0]))
