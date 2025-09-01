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
    bool hasCycle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast) return true;
        }

        return false;
    }
};

int main() {
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = head->next;  // create a cycle

    Solution sol;
    assert(sol.hasCycle(head) == true);

    cout << "All test cases passed." << endl;

    // Clean up memory
    for (ListNode* curr = head; curr != nullptr;) {
        ListNode* temp = curr;
        curr = curr->next;
        delete temp;
    }

    return 0;
}