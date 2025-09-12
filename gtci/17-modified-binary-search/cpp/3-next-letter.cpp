#include <cassert>
#include <iostream>
#include <vector>

class Solution {
public:
  char searchNextLetter(const std::vector<char>& letters, char key) {
    int left = 0;
    int right = letters.size() - 1;
    int ceiling = 0;

    while (left <= right) {
      const int mid = left + (right - left) / 2;

      if (letters[mid] == key) {
        return mid + 1 < letters.size()
          ? letters[mid + 1]
          : letters[0];
      } else if (letters[mid] < key) {
        left = mid + 1;
      } else if (letters[mid] > key) {
        ceiling = mid;
        right = mid - 1;
      }
    }

    return letters[ceiling];
  }
};

int main() {
    Solution s;

    std::vector<char> letters1 {'a', 'c', 'f', 'h'};
    char key1 = 'f';
    assert(s.searchNextLetter(letters1, key1) == 'h');

    std::vector<char> letters2 {'a', 'c', 'f', 'h'};
    char key2 = 'b';
    assert(s.searchNextLetter(letters2, key2) == 'c');

    std::vector<char> letters3 {'a', 'c', 'f', 'h'};
    char key3 = 'm';
    assert(s.searchNextLetter(letters3, key3) == 'a');

    std::vector<char> letters4 {'a', 'c', 'f', 'h'};
    char key4 = 'h';
    assert(s.searchNextLetter(letters4, key4) == 'a');

    std::cout << "All test cases passed." << std::endl;

    return 0;
}
