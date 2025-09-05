#include <cassert>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
   public:
    int firstUniqChar(string s) {
        std::unordered_map<char, int> freqMap;

        for (char ch : s) freqMap[ch] += 1;

        for (int i = 0; i < s.size(); i++) {
            if (freqMap[s[i]] == 1) return i;
        }

        return -1;
    }
};

int main() {
    Solution sol;

    assert(sol.firstUniqChar("leetcode") == 0);
    assert(sol.firstUniqChar("abcab") == 2);
    assert(sol.firstUniqChar("abab") == -1);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
