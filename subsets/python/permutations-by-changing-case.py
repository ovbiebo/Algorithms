def find_letter_case_string_permutations(str):
    permutations = [str]

    for i in range(len(str)):
        curr_len = len(permutations)
        for j in range(curr_len):
            curr_str = permutations[j]
            if curr_str[i].isalpha():
                l, r = curr_str[0: i], curr_str[i + 1: len(curr_str)]
                new_str = l + curr_str[i].swapcase() + r
                permutations.append(new_str)

    return permutations


if __name__ == '__main__':
    print(f"string permutations are: {find_letter_case_string_permutations('ad52')}")
    print(f"string permutations are: {find_letter_case_string_permutations('ab7c')}")
