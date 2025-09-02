#include <algorithm>
#include <iostream>
#include <vector>

#include "interval.h"
#include "util.h"

using namespace std;

class Solution {
   public:
    vector<Interval> merge(vector<Interval>&& intervals) {
        if (intervals.size() < 2) return intervals;

        vector<Interval> mergedIntervals;

        std::sort(intervals.begin(), intervals.end(),
                  [](Interval a, Interval b) { return a.start < b.start; });

        int start = intervals[0].start;
        int end = intervals[0].end;
        for (size_t i = 1; i < intervals.size(); i++) {
            Interval& currentInterval = intervals[i];

            if (currentInterval.start <= end)
                end = std::max(end, currentInterval.end);
            else {
                mergedIntervals.push_back(Interval(start, end));

                start = currentInterval.start;
                end = currentInterval.end;
            }
        }

        mergedIntervals.push_back(Interval(start, end));

        return mergedIntervals;
    }
};

int main() {
    Solution sol;

    // Test case 1: Overlapping intervals
    vector<Interval> result1 = sol.merge(
        vector<Interval>({Interval(1, 4), Interval(2, 5), Interval(7, 9)}));
    assert_equal_interval(result1[0], Interval(1, 5));
    assert_equal_interval(result1[1], Interval(7, 9));
    assert(result1.size() == 2);

    // Test case 2: Non-overlapping and overlapping intervals
    vector<Interval> result2 = sol.merge(
        vector<Interval>({Interval(6, 7), Interval(2, 4), Interval(5, 9)}));
    assert_equal_interval(result2[0], Interval(2, 4));
    assert_equal_interval(result2[1], Interval(5, 9));
    assert(result2.size() == 2);

    // Test case 3: All intervals merge into one
    vector<Interval> result3 = sol.merge(
        vector<Interval>({Interval(1, 4), Interval(2, 6), Interval(3, 5)}));
    assert_equal_interval(result3[0], Interval(1, 6));
    assert(result3.size() == 1);

    cout << "All test cases passed." << endl;

    return 0;
}
