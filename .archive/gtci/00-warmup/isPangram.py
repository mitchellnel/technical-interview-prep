def checkIfPangram(sentence):
    appears = set()

    for char in sentence:
        if char.isalpha():
            appears.add(char.lower())

    return len(appears) == 26


def main():
    # Test cases

    # Test case 1: "TheQuickBrownFoxJumpsOverTheLazyDog"
    # Expected output: True
    print(checkIfPangram("TheQuickBrownFoxJumpsOverTheLazyDog"))

    # Test case 2: "This is not a pangram"
    # Expected output: False
    print(checkIfPangram("This is not a pangram"))

    # Test case 3: "abcdef ghijkl mnopqr stuvwxyz"
    # Expected output: True
    print(checkIfPangram("abcdef ghijkl mnopqr stuvwxyz"))

    # Test case 4: ""
    # Expected output: False
    print(checkIfPangram(""))

    # Test case 5: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Expected output: True
    print(checkIfPangram("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))


main()
