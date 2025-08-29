def isAnagram(s, t):
    if len(s) != len(t):
        return False

    char_counts = {}
    for ch in s:
        if ch not in char_counts:
            char_counts[ch] = 0
        char_counts[ch] += 1

    for ch in t:
        if ch not in char_counts:
            return False

        char_counts[ch] -= 1

    for _, count in char_counts.items():
        if count != 0:
            return False

    return True


if __name__ == "__main__":
    s1 = "listen"
    t1 = "silent"
    print(isAnagram(s1, t1))  # Expected output: True

    s2 = "hello"
    t2 = "world"
    print(isAnagram(s2, t2))  # Expected output: False

    s3 = "anagram"
    t3 = "nagaram"
    print(isAnagram(s3, t3))  # Expected output: True

    s4 = "rat"
    t4 = "car"
    print(isAnagram(s4, t4))  # Expected output: False

    s5 = ""
    t5 = ""
    print(isAnagram(s5, t5))  # Expected output: True
