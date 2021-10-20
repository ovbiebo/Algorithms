from collections import deque


def find_permutations(nums):
    permutations = deque()
    permutations.append([])
    for i in range(len(nums)):
        for j in range(len(permutations)):
            old_perm = permutations.popleft()
            for k in range(len(old_perm) + 1):
                new_perm = old_perm.copy()
                new_perm.insert(k, nums[i])
                permutations.append(new_perm)

    return list(permutations)


if __name__ == '__main__':
    print(f"Here are all the permutations: {find_permutations([1, 3, 5])}")
