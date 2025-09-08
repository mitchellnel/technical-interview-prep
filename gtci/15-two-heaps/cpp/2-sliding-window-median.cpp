#include <cassert>
#include <iostream> 
#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  virtual vector<double> findSlidingWindowMedian(const vector<int> &nums, int k) {
    vector<double> medians;

    MedianFinder mf = MedianFinder();

    int windowStart = 0;
    for (int windowEnd = 0; windowEnd < nums.size(); windowEnd++) {
        if (windowEnd >= k) {
            medians.push_back(mf.getMedian());

            mf.deleteNum(nums[windowStart]);
            windowStart++;
        }

        mf.insertNum(nums[windowEnd]);
    }

    medians.push_back(mf.getMedian());

    return medians;
  }
private:
  class MedianFinder {
    public:
      std::priority_queue<int, std::vector<int>> maxHeap;
      std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

      std::unordered_map<int, int> lazyDeletions;

      void insertNum(const int num) {
        if (maxHeap.empty() || num <= maxHeap.top())
            maxHeap.push(num);
        else
            minHeap.push(num);
        
        rebalanceHeaps();
      }

      void deleteNum(const int num) {
        lazyDeletions[num] += 1;

        cleanMaxHeapTop();
        cleanMinHeapTop();

        rebalanceHeaps();
      }

      double getMedian() {
        cleanMaxHeapTop();
        cleanMinHeapTop();

        if (maxHeap.size() > minHeap.size())
            return maxHeap.top();
        else if (minHeap.size() > maxHeap.size())
            return minHeap.top();
        else
            return (maxHeap.top() + minHeap.top()) / 2.0;
      }

      void rebalanceHeaps() {
        if (maxHeap.size() == minHeap.size())
            return;
        
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size() + 1) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
      }

      void cleanMaxHeapTop() {
        while (!maxHeap.empty()) {
            if (lazyDeletions[maxHeap.top()] > 0) {
                lazyDeletions[maxHeap.top()]--;
                maxHeap.pop();
            } else {
                break;
            }
        }
      }

      void cleanMinHeapTop() {
        while (!minHeap.empty()) {
            if (lazyDeletions[minHeap.top()] > 0) {
                lazyDeletions[minHeap.top()]--;
                minHeap.pop();
            } else {
                break;
            }
        }
      }
  };
};

int main() {
    Solution sol;
    
    vector<double> result = sol.findSlidingWindowMedian({1, 2, -1, 3, 5}, 2);
    vector<double> expected = {1.5, 0.5, 1.0, 4.0};
    assert(result == expected);
    
    result = sol.findSlidingWindowMedian({1, 2, -1, 3, 5}, 3);
    expected = {1.0, 2.0, 3.0};
    assert(result == expected);
    
    cout << "All test cases passed." << endl;
    return 0;
}
