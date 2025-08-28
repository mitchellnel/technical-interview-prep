def backspaceCompare(str1, str2):
    idx1 = len(str1) - 1
    idx2 = len(str2) - 1

    while idx1 >= 0 or idx2 >= 0:
        valid1 = getNextValidCharIndex(str1, idx1)
        valid2 = getNextValidCharIndex(str2, idx2)

        if valid1 < 0 and valid2 < 0:
            # reached the end of both strings
            return True

        if valid1 < 0 or valid2 < 0:
            # reached the end of only one string
            return False

        if str1[valid1] != str2[valid2]:
            # mismatched valid character
            return False

        idx1 = valid1 - 1
        idx2 = valid2 - 1

    return True


def getNextValidCharIndex(str, idx):
    backspace_count = 0
    while idx >= 0:
        if str[idx] == "#":
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            return idx

        idx -= 1

    return idx


def main():
    print(backspaceCompare("xy#z", "xzz#"))
    print(backspaceCompare("xy#z", "xyz#"))
    print(backspaceCompare("xp#", "xyz##"))
    print(backspaceCompare("xywrrmp", "xywrrmu#p"))


main()
