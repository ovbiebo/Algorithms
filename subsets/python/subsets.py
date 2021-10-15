def find_subsets(nums):
    subsets = [[]]

    for number in nums:
        current_subsets_length = len(subsets)
        for i in range(current_subsets_length):
            next_subset = subsets[i].copy()
            next_subset.append(number)
            subsets.append(next_subset)

    return subsets


if __name__ == '__main__':
    print(f"Here is the list of subsets {find_subsets([1, 3])}")
    print(f"Here is the list of subsets {find_subsets([1, 5, 3])}")
