#include <algorithm>
#include <cassert>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Meeting {
   public:
    int start = 0;
    int end = 0;

    Meeting(int start, int end) {
        this->start = start;
        this->end = end;
    }
};

class Solution {
   public:
    int findMinimumMeetingRooms(vector<Meeting>&& meetings) {
        if (meetings.size() < 1) return static_cast<int>(meetings.size());

        std::sort(meetings.begin(), meetings.end(),
                  [](Meeting a, Meeting b) { return a.start < b.start; });

        int minRooms = 0;

        auto meetingCmp = [](const Meeting& a, const Meeting& b) {
            return a.end > b.end;
        };
        std::priority_queue<Meeting, std::vector<Meeting>, decltype(meetingCmp)>
            minHeap(meetingCmp);

        for (Meeting& meeting : meetings) {
            while (!minHeap.empty() && minHeap.top().end <= meeting.start)
                minHeap.pop();

            minHeap.push(meeting);

            minRooms = std::max(minRooms, static_cast<int>(minHeap.size()));
        }

        return minRooms;
    }
};

int main() {
    Solution sol;

    assert(sol.findMinimumMeetingRooms(
               {Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)}) == 2);
    assert(sol.findMinimumMeetingRooms(
               {Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)}) == 1);
    assert(sol.findMinimumMeetingRooms(
               {Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)}) == 2);
    assert(sol.findMinimumMeetingRooms({Meeting(4, 5), Meeting(2, 3),
                                        Meeting(2, 4), Meeting(3, 5)}) == 2);

    cout << "All test cases passed." << endl;

    return 0;
}
