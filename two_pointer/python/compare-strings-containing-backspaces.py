def backspace_compare(str1, str2):
    str1_pt, str2_pt = len(str1) - 1, len(str2) - 1

    while str1_pt > -1 and str2_pt > -1:
        str1_backspaces = 0
        while str1[str1_pt] == "#":
            str1_backspaces += 1
            str1_pt -= 1

        while str1_backspaces > 0:
            str1_backspaces -= 1
            str1_pt -= 1

        str2_backspaces = 0
        while str2[str2_pt] == "#":
            str2_backspaces += 1
            str2_pt -= 1

        while str2_backspaces > 0:
            str2_backspaces -= 1
            str2_pt -= 1

        if str1[str1_pt] == str2[str2_pt]:
            str1_pt -= 1
            str2_pt -= 1
        else:
            return False

    return True if str1_pt == str2_pt else False


if __name__ == '__main__':
    print(backspace_compare("xy#z", "xzz#"))  # true
    print(backspace_compare("xy#z", "xyz#"))  # false
    print(backspace_compare("xp#", "xyz##"))  # true
    print(backspace_compare("xywrrmp", "xywrrmu#p"))  # true
