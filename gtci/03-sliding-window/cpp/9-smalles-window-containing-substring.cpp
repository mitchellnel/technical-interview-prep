#include <cassert>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
   public:
    string findSubstring(const string& str, const string& pattern) {
        std::unordered_map<char, int> pattern_chars =
            Solution::constructFreqMapFromString(pattern);

        int smallest_subarray_size = std::numeric_limits<int>::max();
        int smallest_subarray_start = -1;

        std::unordered_map<char, int> chars;
        int windowStart = 0;
        for (int windowEnd = 0; windowEnd < str.size(); windowEnd++) {
            int windowSize = windowEnd - windowStart + 1;

            chars[str[windowEnd]] += 1;

            while (Solution::isSubmap(pattern_chars, chars)) {
                if (smallest_subarray_size > windowSize) {
                    smallest_subarray_size = windowSize;
                    smallest_subarray_start = windowStart;
                }

                chars[str[windowStart]]--;

                windowStart++;
                windowSize = windowEnd - windowStart + 1;
            }
        }

        return smallest_subarray_start != -1
                   ? str.substr(smallest_subarray_start, smallest_subarray_size)
                   : "";
    }

   private:
    static std::unordered_map<char, int> constructFreqMapFromString(
        const std::string& str) {
        std::unordered_map<char, int> chars;

        for (char ch : str) chars[ch] += 1;

        return chars;
    }

    template <typename K, typename V>
    static bool isSubmap(const std::unordered_map<K, V>& small,
                         const std::unordered_map<K, V>& big) {
        for (const auto& [key, value] : small) {
            auto itr = big.find(key);
            if (itr == big.end() || itr->second < value) return false;
        }

        return true;
    }
};

int main() {
    Solution sol;

    assert(sol.findSubstring("aabdec", "abc") == "abdec");
    assert(sol.findSubstring("aabdec", "abac") == "aabdec");
    assert(sol.findSubstring("abdbca", "abc") == "bca");
    assert(sol.findSubstring("adcad", "abc") == "");

    std::cout << "All test cases passed." << std::endl;
    return 0;
}
