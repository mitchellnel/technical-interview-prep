#include <cassert>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
  // larger half
  std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

  // smaller half
  std::priority_queue<int, std::vector<int>> maxHeap;

  double median;

  void insertNum(int num) {
    if (maxHeap.empty() || num <= maxHeap.top()) {
      maxHeap.push(num);
    } else {
      minHeap.push(num);
    }

    rebalanceHeaps();
    recalculateMedian();
  }

  double findMedian() {
    return median;
  }

private:
  void rebalanceHeaps() {
    if (minHeap.size() == maxHeap.size())
      return;
    
    if (minHeap.size() > maxHeap.size() + 1) {
      maxHeap.push(minHeap.top());
      minHeap.pop();
    } else if (maxHeap.size() > minHeap.size() + 1) {
      minHeap.push(maxHeap.top());
      maxHeap.pop();
    }
  }

  void recalculateMedian() {
    if (minHeap.size() > maxHeap.size())
      median = minHeap.top();
    else if (maxHeap.size() > minHeap.size())
      median = maxHeap.top();
    else
      median = (minHeap.top() + maxHeap.top()) / 2.0;
  }

};

int main() {
    Solution sol;
    
    sol.insertNum(3);
    sol.insertNum(1);
    assert(sol.findMedian() == 2.0);
    
    sol.insertNum(5);
    assert(sol.findMedian() == 3.0);
    
    sol.insertNum(4);
    assert(sol.findMedian() == 3.5);
    
    cout << "All test cases passed." << endl;
    return 0;
}
