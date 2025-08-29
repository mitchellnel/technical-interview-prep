def reverseVowels(self, s: str) -> str:
    s_list = list(s)
    vowels = {"a", "e", "i", "o", "u"}
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left].lower() not in vowels:
            left += 1

        if s[right].lower() not in vowels:
            right -= 1

        if s[left].lower() in vowels and s[right].lower() in vowels:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

    return "".join(s_list)


if __name__ == "__main__":
    print(reverseVowels(None, "hello"))  # holle
    print(reverseVowels(None, "AEOIU"))  # UOIEA
    print(reverseVowels(None, "DesignGUrus"))  # DusUgnGires
