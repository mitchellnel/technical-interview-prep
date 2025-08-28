class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric
        s = "".join(filter(str.isalnum, s)).lower()

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True


def main():
    soln = Solution()

    print("A man, a plan, a canal: Panama")
    print(soln.isPalindrome("A man, a plan, a canal: Panama"))

    print("race a car")
    print(soln.isPalindrome("race a car"))

    print(" ")
    print(soln.isPalindrome(" "))


main()
