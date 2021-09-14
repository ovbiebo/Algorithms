def search_triplets(arr, target):
    closest_sum = float('inf')

    arr.sort()

    i = 0
    while i < len(arr) - 2:
        j = arr[i]
        target_sum = target - j
        l, r = i + 1, len(arr) - 1
        current_sum = 0
        while l < r:
            current_sum = arr[l] + arr[r]
            if current_sum == target_sum:
                return target
            elif current_sum > target_sum:
                r -= 1
            else:
                l += 1
        closest_sum = current_sum + j if abs(target - (current_sum + j)) < abs(target - closest_sum) else closest_sum
        i += 1

    return closest_sum


if __name__ == '__main__':
    print(search_triplets([-2, 0, 1, 2], 2))
    print(search_triplets([-3, -1, 1, 2], 1))
    print(search_triplets([1, 0, 1, 1], 100))
