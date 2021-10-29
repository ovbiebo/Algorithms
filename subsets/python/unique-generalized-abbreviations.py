def generate_generalized_abbreviation(word):
    result = [[*word]]

    for i in range(len(word)):
        res_len = len(result)
        for j in range(res_len):
            new_abbr = result[j].copy()
            if i > 0 and new_abbr[i - 1].isdigit():
                new_abbr[i] = f"{int(new_abbr[i - 1]) + 1}"
                new_abbr[i - 1] = ""
            else:
                new_abbr[i] = "1"
            result.append(new_abbr)

    for i in range(len(result)):
        result[i] = "".join(result[i])

    return result


if __name__ == '__main__':
    print(f"Generalized abbreviation are: {generate_generalized_abbreviation('BAT')}")
    print(f"Generalized abbreviation are: {generate_generalized_abbreviation('code')}")
