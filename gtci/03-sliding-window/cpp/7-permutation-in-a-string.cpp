#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
   public:
    bool findPermutation(const string &str, const string &pattern) {
        std::unordered_map<char, int> pattern_chars =
            Solution::constructFrequencyMapFromString(pattern);

        int windowStart = 0;
        std::unordered_map<char, int> chars;
        for (int windowEnd = 0; windowEnd < str.size(); windowEnd++) {
            int windowSize = windowEnd - windowStart + 1;

            chars[str[windowEnd]] += 1;

            while (windowSize > pattern.size()) {
                chars[str[windowStart]] -= 1;
                if (chars[str[windowStart]] == 0) chars.erase(str[windowStart]);

                windowStart++;
                windowSize = windowEnd - windowStart + 1;
            }

            if (chars == pattern_chars) return true;
        }

        return false;
    }

   private:
    static std::unordered_map<char, int> constructFrequencyMapFromString(
        const std::string &str) {
        std::unordered_map<char, int> chars;
        for (char ch : str) chars[ch] += 1;

        return chars;
    }
};

int main() {
    Solution sol;

    assert(sol.findPermutation("oidbcaf", "abc") == true);
    assert(sol.findPermutation("odicf", "dc") == false);
    assert(sol.findPermutation("bcdxabcdy", "bcdyabcdx") == true);
    assert(sol.findPermutation("aaacb", "abc") == true);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
