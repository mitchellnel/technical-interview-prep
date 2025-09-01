class Solution:
    def findLength(self, fruits):
        max_length = 0

        window_start = 0
        basket = {}
        for window_end in range(len(fruits)):
            if fruits[window_end] not in basket:
                basket[fruits[window_end]] = 0
            basket[fruits[window_end]] += 1

            if len(basket) <= 2:
                max_length = max(max_length, window_end - window_start + 1)

            while len(basket) > 2:
                basket[fruits[window_start]] -= 1
                if basket[fruits[window_start]] == 0:
                    del basket[fruits[window_start]]

                window_start += 1

        return max_length


if __name__ == "__main__":
    sol = Solution()
    assert sol.findLength(["A", "B", "C", "A", "C"]) == 3
    assert sol.findLength(["A", "B", "C", "B", "B", "C"]) == 5
    assert sol.findLength(["A", "A", "A", "A"]) == 4

    print("All test cases passed.")
