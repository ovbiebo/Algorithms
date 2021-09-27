def insert(intervals, new_interval):
    i = 0
    while new_interval[0] > intervals[i][0]:
        i += 1

    intervals.insert(i, new_interval)
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[len(merged) - 1][1]:
            merged[len(merged) - 1][1] = max(intervals[i][1], intervals[i - 1][1])
        else:
            merged.append(intervals[i])

    return merged


if __name__ == '__main__':
    print(f"Interval after insserting the new interval: {str(insert([[1, 3], [5, 7], [8, 12]], [4, 6]))}")
    print(f"Interval after insserting the new interval: {str(insert([[1, 3], [5, 7], [8, 12]], [4, 10]))}")
    print(f"Interval after insserting the new interval: {str(insert([[2, 3], [5, 7]], [1, 4]))}")
