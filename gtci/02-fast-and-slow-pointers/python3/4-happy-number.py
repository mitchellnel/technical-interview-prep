class Solution:
    def find(self, num):
        slow = num
        fast = num
        while True:
            slow = self.calculate_square_sum(slow)
            fast = self.calculate_square_sum(self.calculate_square_sum(fast))

            if slow == fast:
                break

        return slow == 1

    def calculate_square_sum(self, num):
        square_sum = 0
        while num > 0:
            digit = num % 10
            square_sum += digit**2

            num //= 10

        return square_sum


if __name__ == "__main__":
    sol = Solution()
    assert sol.find(23) == True
    assert sol.find(12) == False
