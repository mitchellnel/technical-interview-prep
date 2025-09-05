class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_freq_map = {}
        for char in "balloon":
            if char not in balloon_freq_map:
                balloon_freq_map[char] = 0
            balloon_freq_map[char] += 1

        text_freq_map = {}
        for char in text:
            if char not in text_freq_map:
                text_freq_map[char] = 0
            text_freq_map[char] += 1

        min_count = float("inf")
        for char in balloon_freq_map:
            if char not in text_freq_map:
                return 0

            text_multiple = text_freq_map[char] // balloon_freq_map[char]

            min_count = min(min_count, text_multiple)

        return min_count


if __name__ == "__main__":
    sol = Solution()

    assert sol.maxNumberOfBalloons("nlaebolko") == 1
    assert sol.maxNumberOfBalloons("loonbalxballpoon") == 2
    assert sol.maxNumberOfBalloons("leetcode") == 0
    assert sol.maxNumberOfBalloons("balloonballoon") == 2
    assert sol.maxNumberOfBalloons("balloonballoooon") == 2
    assert sol.maxNumberOfBalloons("bbaall") == 0

    print("All test cases passed.")
