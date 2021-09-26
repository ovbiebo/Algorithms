class interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print(f"[{self.start},{self.end}]", end='')


def merge(intervals):
    intervals.sort(key=lambda a: a.start)
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i - 1].end >= intervals[i].start:
            merged[len(merged) - 1].end = max(intervals[i - 1].end, intervals[i].end)
        else:
            merged.append(intervals[i])

    return merged


if __name__ == '__main__':
    print("Merged intervals: ", end="")
    for i in merge([interval(1, 4), interval(2, 5), interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end="")
    for i in merge([interval(6, 7), interval(2, 4), interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end="")
    for i in merge([interval(1, 4), interval(2, 6), interval(3, 5)]):
        i.print_interval()
    print()
