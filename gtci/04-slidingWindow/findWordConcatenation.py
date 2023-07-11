def findWordConcatenation(str1, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0

        word_freq[word] += 1

    result_indices = []

    words_count = len(words)
    word_length = len(words[0])

    for i in range(len(str1) - words_count * word_length + 1):
        words_seen = {}

        for j in range(0, words_count):
            curr_word_idx = i + j * word_length

            # get the next word from the string
            curr_word = str1[curr_word_idx : curr_word_idx + word_length]

            if curr_word not in word_freq:
                # break if we don't need this word
                break

            # add this word to the words_seen map
            if curr_word not in words_seen:
                words_seen[curr_word] = 0

            words_seen[curr_word] += 1

            # no need to process further if the word has a higher frequency than required
            if words_seen[curr_word] > word_freq.get(curr_word, 0):
                break

            # store index if we have found all the words
            if j + 1 == words_count:
                result_indices.append(i)

    return result_indices


def main():
    print(findWordConcatenation("catfoxcat", ["cat", "fox"]))
    print(findWordConcatenation("catcatfoxfox", ["cat", "fox"]))


main()
