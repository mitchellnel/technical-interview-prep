class Solution:
    def loopExists(self, arr):
        visited = [False] * len(arr)

        for i in range(len(arr)):
            if not visited[i] and self.has_cycle(arr, i, visited):
                return True

        return False

    def has_cycle(self, arr, start, visited):
        path = set([start])

        slow = start
        fast = start
        is_forward = arr[slow] > 0

        while True:
            slow = self.get_next_index(arr, is_forward, slow)

            fast = self.get_next_index(arr, is_forward, fast)
            if fast != -1:
                fast = self.get_next_index(arr, is_forward, fast)

            if slow == -1 or fast == -1:
                break

            path.add(slow)

            if slow == fast:
                return True

        # mark all indexes in path as visited
        for node in path:
            visited[node] = True

        return False

    def get_next_index(self, arr, is_forward, curr_idx):
        is_next_forward = arr[curr_idx] > 0
        if is_forward != is_next_forward:
            return -1

        next_idx = (curr_idx + arr[curr_idx]) % len(arr)

        # check for 1 element cycle
        if curr_idx == next_idx:
            return -1

        return next_idx


if __name__ == "__main__":
    sol = Solution()

    assert sol.loopExists([1, 2, -1, 2, 2])
    assert sol.loopExists([2, 2, -1, 2])
    assert not sol.loopExists([2, 1, -1, -2])

    print("All test cases passed.")
