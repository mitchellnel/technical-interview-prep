class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        if len(ransomNote) > len(magazine):
            return False

        for char in magazine:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

        for char in ransomNote:
            if char not in letters:
                return False

            letters[char] -= 1

            if letters[char] < 0:
                return False

        return True


def main():
    soln = Solution()

    print('ransomNote = "a"; magazine = "b"')
    print(f"{soln.canConstruct('a', 'b')}")

    print('ransomNote = "aa"; magazine = "ab"')
    print(f"{soln.canConstruct('aa', 'ab')}")

    print('ransomNote = "aa"; magazine = "aab"')
    print(f"{soln.canConstruct('aa', 'aab')}")


main()
