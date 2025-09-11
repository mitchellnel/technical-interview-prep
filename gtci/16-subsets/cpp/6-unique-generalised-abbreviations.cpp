#include <cassert>
#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
  std::vector<std::string> generateGeneralizedAbbreviation(const std::string &word) {
    std::vector<std::string> result;
    
    backtrack(result, word, 0, "", 0);

    return result;
  }
private:
  void backtrack(std::vector<std::string>& result, const std::string& word, const size_t index, std::string path, const int count) {
    // base case
    if (index == word.size()) {
      if (count > 0)
        path += std::to_string(count);
      
      result.push_back(path);
      return;
    }

    // at every step we have two choices:
    // - append the letter
    // - append the number
    //   * if the preceding character is a number, add to it

    // to avoid string slicing, we will not commit a count until we are
    // choosing to commit a letter
    std::string newPath = path;
    if (count > 0)
      newPath += std::to_string(count);
    newPath += word[index];
    backtrack(result, word, index + 1, newPath, 0);

    backtrack(result, word, index + 1, path, count + 1);
  }
};

int main() {
    Solution s;
    
    auto contains = [](const std::vector<std::string>& result, const std::string& abbr) {
        for (const auto& a : result) {
        if (a == abbr) return true;
        }
        return false;
    };
    
    std::vector<std::string> expected1 = {
        "word", "wor1", "wo1d", "wo2", "w1rd", "w1r1", "w2d", "w3",
        "1ord", "1or1", "1o1d", "1o2", "2rd", "2r1", "3d", "4"
    };
    std::vector<std::string> result1 = s.generateGeneralizedAbbreviation("word");
    assert(result1.size() == expected1.size());
    for (const auto& abbr : expected1) {
        assert(contains(result1, abbr));
    }
    
    std::vector<std::string> expected2 = {
        "a", "1"
    };
    std::vector<std::string> result2 = s.generateGeneralizedAbbreviation("a");
    assert(result2.size() == expected2.size());
    for (const auto& abbr : expected2) {
        assert(contains(result2, abbr));
    }
    
    std::cout << "All test cases passed." << std::endl;
    return 0;
}
