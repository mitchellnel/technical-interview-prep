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
    assert shortestDistance(words, "the", "fox") == 3
    words2 = ["a", "c", "d", "b", "a"]
    assert shortestDistance(words2, "a", "b") == 1
    words3 = ["a", "b", "c", "d", "e"]
    assert shortestDistance(words3, "a", "e") == 4
    print("All test cases passed.")
