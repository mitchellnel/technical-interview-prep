#include <cctype>
#include <iostream>
#include <string>
#include <unordered_set>

class Solution {
   public:
    std::string reverseVowels(std::string s) {
        const std::unordered_set<char> vowels{'a', 'e', 'i', 'o', 'u'};

        std::string::iterator left = s.begin();
        std::string::iterator right = s.end() - 1;

        while (left < right) {
            if (vowels.find(tolower(*left)) == vowels.end()) left += 1;

            if (vowels.find(tolower(*right)) == vowels.end()) right -= 1;

            if (vowels.find(tolower(*left)) != vowels.end() &&
                vowels.find(tolower(*right)) != vowels.end()) {
                std::swap(*left, *right);

                left += 1;
                right -= 1;
            }
        }

        return s;
    }
};

#include <cassert>

int main() {
    Solution sol;
    assert(sol.reverseVowels("hello") == "holle");
    assert(sol.reverseVowels("AEIOU") == "UOIEA");
    assert(sol.reverseVowels("DesignGUrus") == "DusUgnGires");
    std::cout << "All test cases passed." << std::endl;
    return 0;
}
