def isAnagram(s, t):
    if len(s) != len(t):
        return False

    letter_freq = {}

    for char in s:
        if char not in letter_freq:
            letter_freq[char] = 0

        letter_freq[char] += 1

    for char in t:
        if char not in letter_freq:
            return False

        letter_freq[char] -= 1

        if letter_freq[char] < 0:
            return False

    # check all freqs are now 0
    for char in letter_freq:
        if letter_freq[char] != 0:
            return False

    return True


def main():
    # Test case 1
    s1 = "listen"
    t1 = "silent"
    print(isAnagram(s1, t1))  # Expected output: True

    # Test case 2
    s2 = "hello"
    t2 = "world"
    print(isAnagram(s2, t2))  # Expected output: False

    # Test case 3
    s3 = "anagram"
    t3 = "nagaram"
    print(isAnagram(s3, t3))  # Expected output: True

    # Test case 4
    s4 = "rat"
    t4 = "car"
    print(isAnagram(s4, t4))  # Expected output: False

    # Test case 5
    s5 = ""
    t5 = ""
    print(isAnagram(s5, t5))  # Expected output: True


main()
