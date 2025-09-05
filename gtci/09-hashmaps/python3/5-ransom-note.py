from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_freq_map = {}
        for char in ransomNote:
            if char not in ransom_note_freq_map:
                ransom_note_freq_map[char] = 0
            ransom_note_freq_map[char] += 1

        magazine_freq_map = {}
        for char in magazine:
            if char not in magazine_freq_map:
                magazine_freq_map[char] = 0
            magazine_freq_map[char] += 1

        for char, count in ransom_note_freq_map.items():
            if char not in magazine_freq_map:
                return False

            if count > magazine_freq_map[char]:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()

    assert sol.canConstruct("hello", "hellworld") == True
    assert sol.canConstruct("notes", "stoned") == True
    assert sol.canConstruct("apple", "pale") == False

    print("All test cases passed.")
