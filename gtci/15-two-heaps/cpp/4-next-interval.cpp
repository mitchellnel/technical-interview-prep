#include <cassert>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Interval {
public:
  int start = 0;
  int end = 0;

  Interval(int start, int end) {
    this->start = start;
    this->end = end;
  }
};

class Solution {
public:
  static vector<int> findNextInterval(const vector<Interval> &intervals) {
    vector<int> result(intervals.size(), -1);

    auto cmp = [](std::pair<int, int>& a, std::pair<int, int>& b) {
      return a.first < b.first;
    };
    
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, decltype(cmp)> startMaxHeap(cmp);
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, decltype(cmp)> endMaxHeap(cmp);

    for (int i = 0; i < intervals.size(); i++) {
      startMaxHeap.push({intervals[i].start, i});
      endMaxHeap.push({intervals[i].end, i});
    }

    while (!endMaxHeap.empty()) {
      const auto& [end, currIntervalIdx] = endMaxHeap.top();
      endMaxHeap.pop();

      int start = -1;
      int nextIntervalIdx = -1;
      while (!startMaxHeap.empty() && startMaxHeap.top().first >= end) {
        start = startMaxHeap.top().first;
        nextIntervalIdx = startMaxHeap.top().second;
        startMaxHeap.pop();
      }

      if (nextIntervalIdx != -1) {
        result[currIntervalIdx] = nextIntervalIdx;
        // we process ends in descending order, so we don't need to put back the
        // start times we already popped

        // push back the last popped start time
        startMaxHeap.push({start, nextIntervalIdx});
      }
    }

    return result;
  }
};

int main() {
    vector<Interval> intervals1 = {Interval(2, 3), Interval(3, 4), Interval(5, 6)};
    vector<int> result1 = Solution::findNextInterval(intervals1);
    assert(result1 == vector<int>({1, 2, -1}));

    vector<Interval> intervals2 = {Interval(1, 4), Interval(2, 3), Interval(3, 4)};
    vector<int> result2 = Solution::findNextInterval(intervals2);
    assert(result2 == vector<int>({-1, 2, -1}));

    vector<Interval> intervals3 = {Interval(1, 2), Interval(2, 3), Interval(3, 4)};
    vector<int> result3 = Solution::findNextInterval(intervals3);
    assert(result3 == vector<int>({1, 2, -1}));

    vector<Interval> intervals4 = {Interval(1, 2)};
    vector<int> result4 = Solution::findNextInterval(intervals4);
    assert(result4 == vector<int>({-1}));

    vector<Interval> intervals5 = {Interval(1, 2), Interval(2, 3), Interval(3, 4), Interval(4, 5)};
    vector<int> result5 = Solution::findNextInterval(intervals5);
    assert(result5 == vector<int>({1, 2, 3, -1}));

    cout << "All test cases passed." << endl;

    return 0;
}
