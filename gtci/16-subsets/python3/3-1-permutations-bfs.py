from collections import deque


class Solution:
    def findPermutations(self, nums):
        queue = deque()
        queue.append([])

        for num in nums:
            next_level = deque()
            while queue:
                permutation = queue.popleft()

                # insert num at every possible location
                for i in range(len(permutation) + 1):
                    new_permutation = permutation[:i] + [num] + permutation[i:]
                    next_level.append(new_permutation)

            queue = next_level

        return list(queue)


if __name__ == "__main__":
    sol = Solution()

    assert set(map(tuple, sol.findPermutations([1, 3]))) == set([(1, 3), (3, 1)])
    assert set(map(tuple, sol.findPermutations([1, 5, 3]))) == set(
        [
            (1, 5, 3),
            (1, 3, 5),
            (5, 1, 3),
            (5, 3, 1),
            (3, 5, 1),
            (3, 1, 5),
        ]
    )

    print("All test cases passed.")
