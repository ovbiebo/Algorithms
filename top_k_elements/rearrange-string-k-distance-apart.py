from heapq import *


def reorganize_string(string, k):
    counts = {}
    for letter in string:
        counts[letter] = counts.get(letter, 0) + 1

    last_occurrences = {}
    max_heap = []
    result = []
    while counts:
        for letter, count in counts.items():
            heappush(max_heap, (-count, letter))

        while max_heap:
            count, letter = heappop(max_heap)
            if letter in last_occurrences and len(result) - last_occurrences[letter] < k:
                return ""
            last_occurrences[letter] = len(result)
            result.append(letter)
            counts[letter] = counts[letter] - 1
            if counts[letter] == 0:
                del counts[letter]

    return "".join(result)


if __name__ == '__main__':
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))
