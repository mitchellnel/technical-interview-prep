#include <cassert>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
   public:
    int longestPalindrome(string s) {
        std::unordered_map<char, int> freqMap;

        for (char ch : s) freqMap[ch] += 1;

        int length = 0;
        bool atLeastOneOddChar = false;
        for (const auto& [_, count] : freqMap) {
            if (count % 2 == 0) {
                length += count;
            } else {
                length += count - 1;
                atLeastOneOddChar = true;
            }
        }

        return atLeastOneOddChar ? length + 1 : length;
    }
};

int main() {
    Solution sol;

    assert(sol.longestPalindrome("abccccdd") == 7);
    assert(sol.longestPalindrome("a") == 1);
    assert(sol.longestPalindrome("bb") == 2);
    assert(sol.longestPalindrome("ccc") == 3);
    assert(sol.longestPalindrome("abcd") == 1);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
