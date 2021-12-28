from heapq import *


def sort_character_by_frequency(string):
    top_letters = ""
    top_letters_heap = []
    frequencies = {}

    for letter in string:
        frequencies[letter] = frequencies.get(letter, 0) + 1

    for letter, frequency in frequencies.items():
        heappush(top_letters_heap, (-frequency, letter))

    while top_letters_heap:
        letter = heappop(top_letters_heap)[1]
        top_letters = top_letters + letter * frequencies[letter]

    return top_letters


if __name__ == '__main__':
    print(f"here are the K frequent numbers: {sort_character_by_frequency('Programming')}")  # rrggmmPiano
    print(f"here are the K frequent numbers: {sort_character_by_frequency('abcbab')}")  # bbbaac
