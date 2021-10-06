def merge(firstList, secondList):
    result = []

    a, b = 0, 0
    while a < len(firstList) and b < len(secondList):
        if firstList[a][0] <= secondList[b][1] and firstList[a][1] >= secondList[b][0]:
            result.append([max(firstList[a][0], secondList[b][0]), min(firstList[a][1], secondList[b][1])])
        if firstList[a][1] < secondList[b][1]:
            a += 1
        else:
            b += 1

    return result


if __name__ == '__main__':
    print(f"Intervals intersections: {merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])}")
    print(f"Intervals intersections: {merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])}")
    print(
        f"Intervals intersections: {merge([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]])}")
