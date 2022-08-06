from heapq import *
from collections import deque


def schedule_tasks(tasks, k):
    frequencies = {}
    for task in tasks:
        frequencies[task] = frequencies.get(task, 0) + 1

    max_heap = []
    for task, frequency in frequencies.items():
        heappush(max_heap, (-frequency, task))

    queue = deque()
    cycles = []
    while max_heap:
        frequency, task = heappop(max_heap)
        cycles.append(task)
        frequencies[task] = frequencies[task] - 1
        last_occurrence = len(cycles) - 1
        if frequencies[task] > 0:
            queue.append((task, last_occurrence))

        if queue and not max_heap:
            task, last_occurrence = queue.popleft()
            while len(cycles) - last_occurrence <= k:
                cycles.append("")
            heappush(max_heap, (-frequencies[task], task))

    return len(cycles)


if __name__ == '__main__':
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'b', 'a'], 3)))
