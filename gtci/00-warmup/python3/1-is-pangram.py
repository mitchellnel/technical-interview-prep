def checkIfPangram(sentence):
    letters = {}

    for letter in sentence:
        if not letter.isalpha():
            continue

        letter_lower = letter.lower()

        if letter_lower not in letters:
            letters[letter_lower] = True

    return len(letters) == 26


if __name__ == "__main__":
    print(checkIfPangram("The quick brown fox jumps over the lazy dog"))  # True
    print(checkIfPangram("You shall not pass!"))  # False
    print(checkIfPangram("Pack my box with five dozen liquor jugs."))  # True
