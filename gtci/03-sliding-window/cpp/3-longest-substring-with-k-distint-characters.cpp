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
        std::unordered_map<char, int> chars;

        for (int windowEnd = 0; windowEnd < str.size(); windowEnd++) {
            chars[str[windowEnd]] += 1;

            if (chars.size() == k)
                maxLength = std::max(maxLength, windowEnd - windowStart + 1);

            while (chars.size() > k) {
                chars[str[windowStart]] -= 1;

                if (chars[str[windowStart]] == 0) chars.erase(str[windowStart]);

                windowStart++;
            }
        }

        return maxLength;
    }
};

int main() {
    Solution sol;

    assert(sol.findLength("araaci", 2) == 4);
    assert(sol.findLength("araaci", 1) == 2);
    assert(sol.findLength("cbbebi", 3) == 5);

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
