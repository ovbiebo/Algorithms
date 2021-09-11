def pair_with_targetsum(arr, target_sum):
    left_pt, right_pt = 0, len(arr) - 1
    while right_pt > left_pt:
        total = arr[right_pt] + arr[left_pt]
        if total == target_sum:
            return [left_pt, right_pt]
        if total > target_sum:
            right_pt -= 1
        else:
            left_pt += 1
    return []


if __name__ == '__main__':
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6)) # [1, 3]
    print(pair_with_targetsum([2, 5, 9, 11], 11)) # [0, 2]
