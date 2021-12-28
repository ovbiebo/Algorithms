def calculate_bitwise_complement(n):
    shifted_num = n
    switch_bit = 0
    while shifted_num != 0:
        shifted_num = shifted_num >> 1
        switch_bit = 1 ^ (switch_bit << 1)

    return switch_bit ^ n


if __name__ == '__main__':
    print(calculate_bitwise_complement(8))  # 7
    print(calculate_bitwise_complement(10))  # 5
