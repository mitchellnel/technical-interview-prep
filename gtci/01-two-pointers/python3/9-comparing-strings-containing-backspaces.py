class Solution:
    def compare(self, str1, str2):
        str1_ptr = len(str1) - 1
        str2_ptr = len(str2) - 1

        while str1_ptr >= 0 or str2_ptr >= 0:
            str1_ptr = self.get_next_valid_char(str1, str1_ptr)
            str2_ptr = self.get_next_valid_char(str2, str2_ptr)

            if str1_ptr >= 0 and str2_ptr >= 0 and str1[str1_ptr] != str2[str2_ptr]:
                return False

            str1_ptr -= 1
            str2_ptr -= 1

        return str1_ptr == str2_ptr

    def get_next_valid_char(self, s, i):
        backspace_count = 0
        while i >= 0:
            if s[i] == "#":
                backspace_count += 1
            elif backspace_count > 0:
                backspace_count -= 1
            else:
                return i

            i -= 1

        return i


if __name__ == "__main__":
    sol = Solution()
    assert sol.compare("xy#z", "xzz#") == True
    assert sol.compare("xy#z", "xyz#") == False
    assert sol.compare("xp#", "xyz##") == True
    print("All test cases passed.")
