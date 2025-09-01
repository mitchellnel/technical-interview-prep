#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<int> findStringAnagrams(const string &str, const string &pattern) {
        vector<int> resultIndices;

        std::unordered_map<char, int> pattern_chars =
            Solution::constructFreqMapFromString(pattern);

        std::unordered_map<char, int> chars;
        int windowStart = 0;
        for (int windowEnd = 0; windowEnd < str.size(); windowEnd++) {
            int windowSize = windowEnd - windowStart + 1;

            chars[str[windowEnd]] += 1;

            while (windowSize > pattern.size()) {
                chars[str[windowStart]] -= 1;
                if (chars[str[windowStart]] == 0) chars.erase(str[windowStart]);

                windowStart++;
                windowSize = windowEnd - windowStart + 1;
            }

            if (windowSize == pattern.size() && chars == pattern_chars)
                resultIndices.push_back(windowStart);
        }

        return resultIndices;
    }

   private:
    static std::unordered_map<char, int> constructFreqMapFromString(
        const std::string &str) {
        std::unordered_map<char, int> chars;

        for (char ch : str) chars[ch] += 1;

        return chars;
    }
};

int main() {
    Solution sol;

    assert(sol.findStringAnagrams("ppqp", "pq") == vector<int>({1, 2}));
    assert(sol.findStringAnagrams("abbcabc", "abc") == vector<int>({2, 3, 4}));

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
