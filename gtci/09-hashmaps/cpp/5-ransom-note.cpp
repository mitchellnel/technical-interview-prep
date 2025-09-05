#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
   public:
    bool canConstruct(string ransomNote, string magazine) {
        std::unordered_map<char, int> ransomNoteFreqMap;
        for (char ch : ransomNote) ransomNoteFreqMap[ch] += 1;

        std::unordered_map<char, int> magazineFreqMap;
        for (char ch : magazine) magazineFreqMap[ch] += 1;

        for (const auto& [ch, count] : ransomNoteFreqMap) {
            if (!magazineFreqMap.contains(ch)) return false;

            if (count > magazineFreqMap[ch]) return false;
        }

        return true;
    }
};

int main() {
    Solution sol;

    assert(sol.canConstruct("hello", "hellworld") == true);
    assert(sol.canConstruct("notes", "stoned") == true);
    assert(sol.canConstruct("apple", "pale") == false);

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
