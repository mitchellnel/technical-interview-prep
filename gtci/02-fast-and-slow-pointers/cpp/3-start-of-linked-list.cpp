#include <cassert>
#include <iostream>

using namespace std;

class ListNode {
   public:
    int val = 0;
    ListNode* next;

    ListNode(int value) {
        this->val = value;
        next = nullptr;
    }
};

class Solution {
   public:
    ListNode* findCycleStart(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        int cycleLength = 0;
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast) {
                cycleLength = Solution::calculateLengthOfCycle(slow);
                break;
            }
        }

        slow = head;
        fast = head;
        while (cycleLength > 0) {
            fast = fast->next;
            cycleLength--;
        }

        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }

        return slow;
    }

   private:
    static int calculateLengthOfCycle(ListNode* cycleStart) {
        int cycleLength = 0;
        ListNode* curr = cycleStart;

        do {
            cycleLength++;
            curr = curr->next;
        } while (curr != cycleStart);

        return cycleLength;
    }
};

int main() {
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    head->next->next->next->next->next = head->next;

    Solution sol;
    assert(sol.findCycleStart(head)->val == 2);

    cout << "All test cases passed." << endl;

    // Clean up memory
    for (ListNode* curr = head; curr != nullptr;) {
        ListNode* temp = curr;
        curr = curr->next;
        delete temp;
    }

    return 0;
}
