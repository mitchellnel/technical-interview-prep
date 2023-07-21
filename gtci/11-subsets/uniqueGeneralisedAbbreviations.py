from collections import deque


class AbbreviatedWord:
    def __init__(self, string, start, count):
        self.string = string
        self.start = start
        self.count = count


def generate_generalised_abbreviations(word):
    abbreviations = []

    queue = deque([AbbreviatedWord(list(), 0, 0)])
    while len(queue) > 0:
        ab_word = queue.popleft()

        if ab_word.start == len(word):
            if ab_word.count != 0:
                ab_word.string.append(str(ab_word.count))

            abbreviations.append("".join(ab_word.string))
            continue

        # continue abbreviating by incrementing the current abbreviation count
        queue.append(
            AbbreviatedWord(list(ab_word.string), ab_word.start + 1, ab_word.count + 1)
        )

        # restart abbreviation, append the count and current char to the string
        if ab_word.count != 0:
            ab_word.string.append(str(ab_word.count))

        new_word = list(ab_word.string)
        new_word.append(word[ab_word.start])

        queue.append(AbbreviatedWord(new_word, ab_word.start + 1, 0))

    return abbreviations


def generate_generalised_abbreviations_recursive(word):
    abbreviations = []

    generate_generalised_abbreviations_recursive_helper(
        word, list(), 0, 0, abbreviations
    )

    return abbreviations


def generate_generalised_abbreviations_recursive_helper(
    word, ab_word, start, count, abbreviations
):
    if start == len(word):
        if count != 0:
            ab_word.append(str(count))

        abbreviations.append("".join(ab_word))

        return

    # continue abbreviating by incrementing the current abbreviation count
    generate_generalised_abbreviations_recursive_helper(
        word, list(ab_word), start + 1, count + 1, abbreviations
    )

    # restart abbreviation, append the count and current char to the string
    if count != 0:
        ab_word.append(str(count))

    new_word = list(ab_word)
    new_word.append(word[start])

    generate_generalised_abbreviations_recursive_helper(
        word, new_word, start + 1, 0, abbreviations
    )


def main():
    print(
        "Generalized abbreviation are: "
        + str(generate_generalised_abbreviations("BAT"))
    )
    print(
        "Generalized abbreviation are: "
        + str(generate_generalised_abbreviations("code"))
    )


main()
