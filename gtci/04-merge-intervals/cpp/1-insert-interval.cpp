#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

#include "interval.h"
#include "util.h"

using namespace std;

class Solution {
   public:
    vector<Interval> insert(const vector<Interval> &intervals,
                            Interval newInterval) {
        vector<Interval> mergedIntervals;

        size_t idx = 0;

        // find and append all intervals ending before the new interval starts
        while (idx < intervals.size() &&
               intervals[idx].end < newInterval.start) {
            mergedIntervals.push_back(intervals[idx]);
            idx++;
        }

        // merge all intervals overlapping with the new interval
        while (idx < intervals.size() &&
               intervals[idx].start <= newInterval.end) {
            newInterval.start =
                std::min(newInterval.start, intervals[idx].start);
            newInterval.end = std::max(newInterval.end, intervals[idx].end);

            idx++;
        }

        mergedIntervals.push_back(newInterval);

        // append remaining intervals
        while (idx < intervals.size()) {
            mergedIntervals.push_back(intervals[idx]);
            idx++;
        }

        return mergedIntervals;
    }
};

int main() {
    Solution sol;

    vector<Interval> result1 = sol.insert(
        {Interval(1, 3), Interval(5, 7), Interval(8, 12)}, Interval(4, 6));
    assert_equal_interval(result1[0], Interval(1, 3));
    assert_equal_interval(result1[1], Interval(4, 7));
    assert_equal_interval(result1[2], Interval(8, 12));
    assert(result1.size() == 3);

    vector<Interval> result2 = sol.insert(
        {Interval(1, 3), Interval(5, 7), Interval(8, 12)}, Interval(4, 10));
    assert_equal_interval(result2[0], Interval(1, 3));
    assert_equal_interval(result2[1], Interval(4, 12));
    assert(result2.size() == 2);

    vector<Interval> result3 =
        sol.insert({Interval(2, 3), Interval(5, 7)}, Interval(1, 4));
    assert_equal_interval(result3[0], Interval(1, 4));
    assert_equal_interval(result3[1], Interval(5, 7));
    assert(result3.size() == 2);

    cout << "All test cases passed." << endl;

    return 0;
}
