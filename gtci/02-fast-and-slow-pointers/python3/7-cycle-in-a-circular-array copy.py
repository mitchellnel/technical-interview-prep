class Solution:
    def loopExists(self, arr):
        for i in range(len(arr)):
            if self.has_cycle(arr, i):
                return True

        return False

    def has_cycle(self, arr, start):
        slow = start
        fast = start
        is_forward = arr[slow] > 0

        while True:
            slow = self.get_next_index(arr, is_forward, slow)

            fast = self.get_next_index(arr, is_forward, fast)
            if fast != -1:
                fast = self.get_next_index(arr, is_forward, fast)

            if slow == -1 or fast == -1 or slow == fast:
                break

        return slow != -1 and slow == fast

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
