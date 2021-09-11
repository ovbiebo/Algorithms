def make_squares(arr):
    result = []
    left, right = 0, 1

    while arr[right] < 0:
        right += 1
        left += 1

    while right < len(arr) and left > -1:
        left_sqr = arr[left] ** 2
        right_sqr = arr[right] ** 2

        if left_sqr < right_sqr:
            result.append(left_sqr)
            left -= 1
        else:
            result.append(right_sqr)
            right += 1

    # Append all remaining squares
    while right < len(arr):
        result.append(arr[right] ** 2)
        right += 1
    while left > -1:
        result.append(arr[left] ** 2)
        left -= 1

    return result


if __name__ == '__main__':
    print(make_squares([-2, -1, 0, 2, 3]))
    print(make_squares([-3, -1, 0, 1, 2]))
