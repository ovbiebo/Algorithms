import math


def shortest_window_sort(arr):
    if len(arr) == 1:
        return 0

    left_pt, right_pt = 0, 1
    high = None
    low = None

    while right_pt < len(arr):
        if arr[left_pt] > arr[right_pt]:
            high = max(arr[left_pt], (high or -math.inf))
            low = min(arr[right_pt], (low or math.inf))
        right_pt += 1
        left_pt += 1

    left_pt = 0
    while low and arr[left_pt] < low:
        left_pt += 1

    right_pt = len(arr) - 1
    while high and arr[right_pt] > high:
        right_pt -= 1

    return 0 if high is None else right_pt - left_pt + 1


if __name__ == '__main__':
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))
