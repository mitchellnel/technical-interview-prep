class Solution:
    def findWordConcatenation(self, str1, words):
        result_indices = []
        word_length = len(words[0])

        window_start = 0
        window_end = word_length * len(words) - 1
        while window_end < len(str1):
            words_seen = {word: False for word in words}

            nextWordIndex = window_start
            while nextWordIndex <= window_end:
                word = str1[nextWordIndex : nextWordIndex + word_length]
                if word not in words:
                    break

                words_seen[word] = True

                if all(words_seen.values()):
                    result_indices.append(window_start)
                    break

                nextWordIndex += word_length

            window_start += 1
            window_end = window_start + word_length * len(words) - 1

        return result_indices


if __name__ == "__main__":
    sol = Solution()

    assert sol.findWordConcatenation("catfoxcat", ["cat", "fox"]) == [0, 3]
    assert sol.findWordConcatenation("catcatfoxfox", ["cat", "fox"]) == [3]
    assert sol.findWordConcatenation("horsedogcat", ["cat", "dog"]) == [5]

    print("All test cases passed.")
