from heapq import *


def rearrange_string(string):
    counts = {}
    for letter in string:
        counts[letter] = counts.get(letter, 0) + 1

    max_heap = []
    result = []
    while counts:
        for letter, count in counts.items():
            heappush(max_heap, (-count, letter))

        while max_heap:
            count, letter = heappop(max_heap)
            result.append(letter)
            counts[letter] = counts[letter] - 1
            if counts[letter] == 0:
                del counts[letter]
            if len(result) > 1 and letter == result[len(result) - 2]:
                return ""

    return "".join(result)


if __name__ == '__main__':
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))
