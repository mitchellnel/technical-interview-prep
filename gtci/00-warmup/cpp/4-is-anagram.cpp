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

int main() {
    Solution sol;

    std::string s1 = "listen";
    std::string t1 = "silent";
    std::cout << std::boolalpha << sol.isAnagram(s1, t1)
              << std::endl;  // Expected output: True

    std::string s2 = "hello";
    std::string t2 = "world";
    std::cout << std::boolalpha << sol.isAnagram(s2, t2)
              << std::endl;  // Expected output: False

    std::string s3 = "anagram";
    std::string t3 = "nagaram";
    std::cout << std::boolalpha << sol.isAnagram(s3, t3)
              << std::endl;  // Expected output: True

    std::string s4 = "rat";
    std::string t4 = "car";
    std::cout << std::boolalpha << sol.isAnagram(s4, t4)
              << std::endl;  // Expected output: False

    std::string s5 = "";
    std::string t5 = "";
    std::cout << std::boolalpha << sol.isAnagram(s5, t5)
              << std::endl;  // Expected output: True

    return 0;
}
