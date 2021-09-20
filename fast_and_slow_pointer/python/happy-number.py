def find_happy_number(num):
    slow, fast = num, sum_of_squares(sum_of_squares(num))
    while slow != fast:
        if slow == 1 or fast == 1:
            return True
        slow = sum_of_squares(slow)
        fast = sum_of_squares(sum_of_squares(fast))
    return False


def sum_of_squares(num):
    _sum = 0
    for i in str(num):
        _sum += int(i) ** 2
    return _sum


if __name__ == '__main__':
    print(find_happy_number(23))
    print(find_happy_number(12))
