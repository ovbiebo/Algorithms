def find_single_number(arr):
    single_number = 0
    for num in arr:
        single_number ^= num

    return single_number or None


if __name__ == '__main__':
    print(find_single_number([1, 4, 2, 1, 3, 2, 3]))  # 4
    print(find_single_number([7, 9, 7]))  # 9
