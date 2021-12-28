def find_single_numbers(arr):
    single_nums = 0
    for num in arr:
        single_nums ^= num

    test_bit = 1
    while (test_bit & single_nums) == 0:
        test_bit = test_bit << 1

    num_a, num_b = 0, 0
    for num in arr:
        if (test_bit & num) == 0:
            num_a ^= num
        else:
            num_b ^= num

    return [num_a, num_b]


if __name__ == '__main__':
    print(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))  # [4, 6]
    print(find_single_numbers([2, 1, 3, 2]))  # [1, 3]
