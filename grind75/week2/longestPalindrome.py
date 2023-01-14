class Solution:
    def longestPalindrome(self, s: str) -> int:
        single_letters = set()

        for char in s:
            if char not in single_letters:
                single_letters.add(char)
            else:
                single_letters.remove(char)

        # now the length of the longest palindrome is:
        # - len(s) if there are no letters that only occur once
        # - len(s) - len(single_letters) + 1 if there exist letters that
        #    only occur once; this is because we can have at most one of these
        #    letters in our palindrome
        return len(s) - len(single_letters) + 1 if len(single_letters) > 0 else len(s)


def main():
    soln = Solution()

    print(
        f'"abccccdd" --> longest palindrome is {soln.longestPalindrome("abccccdd")} letters'
    )
    print(
        f'"abbsdajgekfdmmmemffemkdsfmfamew" --> longest palindrome is {soln.longestPalindrome("abbsdajgekfdmmmemffemkdsfmfamew")} letters'
    )
    print(f'"a" --> longest palindrome is {soln.longestPalindrome("a")} letters')


main()
