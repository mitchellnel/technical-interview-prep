#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
   public:
    int findLength(const string &str, int k) {
        int maxLength = 0;

        int windowStart = 0;
        int maxLetterFreq = 0;
        std::unordered_map<char, int> chars;
        for (int windowEnd = 0; windowEnd < str.size(); windowEnd++) {
            int windowSize = windowEnd - windowStart + 1;
            chars[str[windowEnd]] += 1;

            maxLetterFreq = std::max(maxLetterFreq, chars[str[windowEnd]]);

            if (windowSize - maxLetterFreq <= k)
                maxLength = std::max(maxLength, windowSize);

            while (windowSize - maxLetterFreq > k) {
                chars[str[windowStart]] -= 1;
                if (chars[str[windowStart]] == 0) chars.erase(str[windowStart]);

                windowStart++;
                windowSize = windowEnd - windowStart + 1;
            }
        }

        return maxLength;
    }
};

int main() {
    Solution sol;

    assert(sol.findLength("aabccbb", 2) == 5);
    assert(sol.findLength("abbcb", 1) == 4);
    assert(sol.findLength("abccde", 1) == 3);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
