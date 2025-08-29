def shortestDistance(words, word1, word2):
    word1_idx = -1
    word2_idx = -1

    shortest_distance = len(words)

    for idx, word in enumerate(words):
        if word == word1:
            word1_idx = idx

            if word2_idx != -1:
                shortest_distance = min(abs(word1_idx - word2_idx), shortest_distance)

        if word == word2:
            word2_idx = idx

            if word1_idx != -1:
                shortest_distance = min(abs(word1_idx - word2_idx), shortest_distance)

        if shortest_distance == 1:
            return 1

    return shortest_distance


if __name__ == "__main__":
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    word1 = "the"
    word2 = "fox"
    print(shortestDistance(words, word1, word2))  # Output: 3

    words2 = ["a", "c", "d", "b", "a"]
    word3 = "a"
    word4 = "b"
    print(shortestDistance(words2, word3, word4))  # Output: 1

    words3 = ["a", "b", "c", "d", "e"]
    word5 = "a"
    word6 = "e"
    print(shortestDistance(words3, word5, word6))  # Output: 4
