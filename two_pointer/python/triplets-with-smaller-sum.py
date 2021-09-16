def triplet_with_smaller_sum(arr, target):
    count = 0

    arr.sort()

    for i in range(len(arr) - 2):
        current_target = target - arr[i]
        left, right = i + 1, len(arr) - 1
        while left < right:
            if arr[left] + arr[right] >= current_target:
                right -= 1
            else:
                count += right - left
                left += 1

    return count

def triplet_with_smaller_sum_ii(arr, target):
    triplets = []

    arr.sort()

    for i in range(len(arr) - 2):
        current_target = target - arr[i]
        left, right = i + 1, len(arr) - 1
        while left < right:
            if arr[left] + arr[right] >= current_target:
                right -= 1
            else:
                for t in range(right, left, -1):
                    triplets.append([arr[i], arr[left], arr[t]])
                left += 1

    return triplets

if __name__ == '__main__':
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
    print(triplet_with_smaller_sum_ii([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum_ii([-1, 4, 2, 1, 3], 5))
