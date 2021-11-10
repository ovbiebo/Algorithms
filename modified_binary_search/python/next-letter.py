def search_next_letter(letters, key):
    start, end = 0, len(letters) - 1

    if key >= letters[-1] or key < letters[0]:
        return letters[0]

    while start <= end:
        mid = start + (end - start) // 2

        # if letters[mid] == key:
        #     return letters[mid + 1]

        if key < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return letters[start]


if __name__ == '__main__':
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'h'))
