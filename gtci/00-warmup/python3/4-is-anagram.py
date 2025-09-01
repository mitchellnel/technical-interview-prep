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
    assert isAnagram("listen", "silent") == True
    assert isAnagram("hello", "world") == False
    assert isAnagram("anagram", "nagaram") == True
    assert isAnagram("rat", "car") == False
    print("All test cases passed.")
