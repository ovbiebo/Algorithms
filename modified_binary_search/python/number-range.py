def find_range(nums, key):
    return [find_bound(nums, key, False), find_bound(nums, key, True)]


def find_bound(nums, key, finding_upper):
    result = -1
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key == nums[mid]:
            result = mid
        if finding_upper:
            if key < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

    return result


if __name__ == '__main__':
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))
