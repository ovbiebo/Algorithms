def find_subsets(nums):
    nums.sort()
    subsets = [[]]
    prev_subsets_length = 1
    for i in range(len(nums)):
        current_subsets_length = len(subsets)
        if nums[i] != nums[i - 1] or i == 0:
            prev_subsets_length = 0
        for j in range(prev_subsets_length, current_subsets_length):
            next_subset = subsets[j].copy()
            next_subset.append(nums[i])
            subsets.append(next_subset)
        prev_subsets_length = current_subsets_length

    return subsets


if __name__ == '__main__':
    print(f"Here is the list of subsets {find_subsets([1])}")
    print(f"Here is the list of subsets {find_subsets([1, 3, 3])}")
    print(f"Here is the list of subsets {find_subsets([1, 5, 3, 3])}")
