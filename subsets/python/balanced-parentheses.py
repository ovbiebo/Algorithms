from collections import deque


def generate_valid_parentheses(nums):
    result = []

    permutations = deque()
    permutations.append(("", 0, 0))

    while permutations:
        (permutation, opens, closes) = permutations.popleft()

        if len(permutation) == nums*2:
            result.append(permutation)

        if opens < nums:
            permutations.append((permutation + "(", opens + 1, closes))
        if opens > closes:
            permutations.append((permutation + ")", opens, closes + 1))

    return result


if __name__ == '__main__':
    print(f"All combinations of balanced parentheses are: {generate_valid_parentheses(2)}")
    print(f"All combinations of balanced parentheses are: {generate_valid_parentheses(3)}")
