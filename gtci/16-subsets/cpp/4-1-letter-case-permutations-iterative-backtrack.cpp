#include <cassert>
#include <cctype>
#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
  std::vector<std::string> findLetterCaseStringPermutations(const std::string& str) {
    std::vector<std::string> permutations;
    backtrack(permutations, str, 0, "");
    return permutations;
  }
private:
  void backtrack(std::vector<std::string>& permutations, const std::string& str, const size_t& index, std::string path) {
    if (index == str.size()) {
      permutations.push_back(path);
      return;
    }

    const char ch = str[index];
    if (std::isalpha(ch)) {
      backtrack(permutations, str, index + 1, path + (char) std::tolower(ch));
      backtrack(permutations, str, index + 1, path + (char) std::toupper(ch));
    } else {
      backtrack(permutations, str, index + 1, path + ch);
    }
  }
};



int main() {
    Solution s;
    
    auto contains = [](const std::vector<std::string>& result, const std::string& subset) {
        for (const auto& s : result) {
        if (s == subset) return true;
        }
        return false;
    };
    
    std::vector<std::string> expected1 = {
        "ad", "aD", "Ad", "AD"
    };
    std::vector<std::string> result1 = s.findLetterCaseStringPermutations("ad");
    assert(result1.size() == expected1.size());
    for (const auto& subset : expected1) {
        assert(contains(result1, subset));
    }
    
    std::vector<std::string> expected2 = {
        "ab", "aB", "Ab", "AB"
    };
    std::vector<std::string> result2 = s.findLetterCaseStringPermutations("ab");
    assert(result2.size() == expected2.size());
    for (const auto& subset : expected2) {
        assert(contains(result2, subset));
    }
    
    std::vector<std::string> expected3 = {
        "3z4", "3Z4"
    };
    std::vector<std::string> result3 = s.findLetterCaseStringPermutations("3z4");
    assert(result3.size() == expected3.size());
    for (const auto& subset : expected3) {
        assert(contains(result3, subset));
    }
    
    std::vector<std::string> expected4 = {
        "12345"
    };
    std::vector<std::string> result4 = s.findLetterCaseStringPermutations("12345");
    assert(result4.size() == expected4.size());
    for (const auto& subset : expected4) {
        assert(contains(result4, subset));
    }
    
    std::cout << "All test cases passed." << std::endl;
    return 0;
}
