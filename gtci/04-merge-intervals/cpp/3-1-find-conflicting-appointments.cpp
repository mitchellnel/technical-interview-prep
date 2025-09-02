#include <algorithm>
#include <cassert>
#include <iostream>
#include <queue>
#include <vector>

#include "interval.h"

using namespace std;

class Solution {
   public:
    vector<pair<Interval, Interval>> getConflictingAppointments(
        vector<Interval>& intervals) {
        vector<pair<Interval, Interval>> conflicts;

        if (intervals.size() < 2) return conflicts;

        std::sort(intervals.begin(), intervals.end(),
                  [](Interval a, Interval b) { return a.start < b.start; });

        // interval comparator function for min-heap
        auto intervalCmp = [](const Interval& a, const Interval& b) {
            return a.end > b.end;  // smaller end comes first
        };

        std::priority_queue<Interval, std::vector<Interval>,
                            decltype(intervalCmp)>
            minHeap(intervalCmp);

        for (Interval& curr : intervals) {
            // pop all intervals that end before the current one starts
            while (!minHeap.empty() && minHeap.top().end <= curr.start)
                minHeap.pop();

            // all remaining intervals overlap
            auto temp = minHeap;
            while (!temp.empty()) {
                conflicts.push_back({temp.top(), curr});
                temp.pop();
            }

            // push the current interval into the heap
            minHeap.push(curr);
        }

        return conflicts;
    }
};

int main() {
    Solution sol;

    vector<Interval> intervals1 = {Interval(4, 5), Interval(2, 3),
                                   Interval(3, 6), Interval(5, 7),
                                   Interval(7, 8)};
    vector<pair<Interval, Interval>> expected = {
        {Interval(3, 6), Interval(4, 5)}, {Interval(3, 6), Interval(5, 7)}};
    auto result = sol.getConflictingAppointments(intervals1);
    assert(result.size() == expected.size());
    for (size_t i = 0; i < result.size(); i++) {
        assert(result[i].first == expected[i].first);
        assert(result[i].second == expected[i].second);
    }

    cout << "All test cases passed." << endl;

    return 0;
}
