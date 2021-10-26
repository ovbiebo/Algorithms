def generate_generalized_abbreviation(word):
    result = []
    substrings = [["_" for i in range(len(word))]]

    for i in range(len(word)):
        substrings_len = len(substrings)
        for j in range(substrings_len):
            substr = substrings[j].copy()
            substr[i] = word[i]
            substrings.append(substr)

    for substr in substrings:
        abbreviation = ""
        spaces = 0
        for i in range(len(substr)):
            if substr[i].isalpha():
                abbreviation = abbreviation + f"{spaces or ''}" + substr[i]
                spaces = 0
            else:
                spaces += 1

        abbreviation = abbreviation + f"{spaces or ''}"
        result.append(abbreviation)

    return result


if __name__ == '__main__':
    print(f"Generalized abbreviation are: {generate_generalized_abbreviation('BAT')}")
    print(f"Generalized abbreviation are: {generate_generalized_abbreviation('code')}")
