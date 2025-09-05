#include <algorithm>
#include <cassert>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
   public:
    int maxNumberOfBalloons(string text) {
        std::unordered_map<char, int> balloonFreqMap = {
            {'b', 1}, {'a', 1}, {'l', 2}, {'o', 2}, {'n', 1}};

        std::unordered_map<char, int> textFreqMap;
        for (char ch : text) textFreqMap[ch] += 1;

        int minCount = std::numeric_limits<int>::max();
        for (const auto& [ch, freq] : balloonFreqMap) {
            if (!textFreqMap.contains(ch)) return 0;

            int textMultiple = textFreqMap[ch] / balloonFreqMap[ch];
            minCount = std::min(minCount, textMultiple);
        }

        return minCount;
    }
};

int main() {
    Solution sol;

    assert(sol.maxNumberOfBalloons("nlaebolko") == 1);
    assert(sol.maxNumberOfBalloons("loonbalxballpoon") == 2);
    assert(sol.maxNumberOfBalloons("leetcode") == 0);
    assert(sol.maxNumberOfBalloons("balloonballoon") == 2);
    assert(sol.maxNumberOfBalloons("balloonballoooon") == 2);
    assert(sol.maxNumberOfBalloons("bbaall") == 0);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
