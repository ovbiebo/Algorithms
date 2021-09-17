def search_quadruplets(arr, target):
    quadruplets = []

    arr.sort()

    for i in range(len(arr) - 3):
        # skip same element to avoid duplicates
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, len(arr) - 2):
            # skip same element to avoid duplicates
            if j > 1 + 1 and arr[j] == arr[j - 1]:
                continue

            current_target = target - arr[i] - arr[j]
            left, right = j + 1, len(arr) - 1

            while left < right:
                if arr[left] + arr[right] == current_target:
                    quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1

                    # skip same element to avoid duplicates
                    while arr[left] == arr[left - 1] and left < right:
                        left += 1
                    # skip same element to avoid duplicates
                    while arr[right] == arr[right + 1] and left < right:
                        right -= 1

                elif arr[left] + arr[right] > current_target:
                    right -= 1

                else:
                    left += 1

    return quadruplets


if __name__ == '__main__':
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))
