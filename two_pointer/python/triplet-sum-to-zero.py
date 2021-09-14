def search_triplets(arr):
    triplets = []

    arr.sort()

    i = 0
    while i < len(arr) - 2:
        j = arr[i]
        target_sum = 0 - j
        l, r = i + 1, len(arr) - 1
        while l < r:
            current_sum = arr[l] + arr[r]
            if current_sum == target_sum:
                while l == l + 1:
                    l += 1
                while r == r - 1:
                    r -= 1
                triplets.append([j, arr[l], arr[r]])
                l += 1
                r -= 1

            elif current_sum > target_sum:
                r -= 1
            else:
                l += 1
        i += 1

    return triplets


if __name__ == '__main__':
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))
