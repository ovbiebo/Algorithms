from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    min_start_heap = []
    min_end_heap = []
    result = [-1 for x in range(len(intervals))]

    for i in range(len(intervals)):
        heappush(min_start_heap, (intervals[i].start, i))
        heappush(min_end_heap, (intervals[i].end, i))

    while min_end_heap:
        interval_end, end_index = heappop(min_end_heap)
        while min_start_heap and min_start_heap[0][0] < interval_end:
            heappop(min_start_heap)
        if min_start_heap:
            result[end_index] = min_start_heap[0][1]

    return result


if __name__ == '__main__':
    result = find_next_interval(
        [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
        [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))
