#include <iostream>
#include <unordered_map>

class Solution {
   public:
    bool isAnagram(std::string s, std::string t) {
        if (s.size() != t.size()) return false;

        std::unordered_map<char, int> char_counts{};

        for (int i = 0; i < s.size(); i++) {
            char_counts[s[i]]++;
            char_counts[t[i]]--;
        }

        for (const std::pair<const char, int>& kv : char_counts) {
            if (kv.second != 0) {
                return false;
            }
        }

        return true;
    }
};

#include <cassert>

int main() {
    Solution sol;
    assert(sol.isAnagram("listen", "silent") == true);
    assert(sol.isAnagram("hello", "world") == false);
    assert(sol.isAnagram("anagram", "nagaram") == true);
    assert(sol.isAnagram("rat", "car") == false);
    std::cout << "All test cases passed." << std::endl;
    return 0;
}
