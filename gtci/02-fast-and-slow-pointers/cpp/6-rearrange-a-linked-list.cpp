#include <cassert>
#include <iostream>
#include <vector>

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
    ListNode* reorder(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        ListNode* middle = getMiddleNode(head);
        ListNode* firstHalfCurr = head;
        ListNode* secondHalfCurr = reverseList(middle);

        while (firstHalfCurr != nullptr && secondHalfCurr != nullptr) {
            ListNode* temp = firstHalfCurr->next;
            firstHalfCurr->next = secondHalfCurr;
            firstHalfCurr = temp;

            temp = secondHalfCurr->next;
            secondHalfCurr->next = firstHalfCurr;
            secondHalfCurr = temp;
        }

        if (firstHalfCurr != nullptr) {
            firstHalfCurr->next = nullptr;
        }

        return head;
    }

    vector<int> getListValues(ListNode* head) {
        vector<int> values;
        ListNode* curr = head;
        while (curr != nullptr) {
            values.push_back(curr->val);
            curr = curr->next;
        }
        return values;
    }

   private:
    ListNode* getMiddleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr != nullptr) {
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }
};

int main() {
    // Test case 1: Even length list [1, 2, 3, 4]
    // Expected result: [1, 4, 2, 3]
    ListNode* head1 = new ListNode(1);
    head1->next = new ListNode(2);
    head1->next->next = new ListNode(3);
    head1->next->next->next = new ListNode(4);

    Solution sol;
    ListNode* reordered1 = sol.reorder(head1);
    vector<int> expected1 = {1, 4, 2, 3};
    assert(sol.getListValues(reordered1) == expected1);

    // Test case 2: Odd length list [1, 2, 3, 4, 5]
    // Expected result: [1, 5, 2, 4, 3]
    ListNode* head2 = new ListNode(1);
    head2->next = new ListNode(2);
    head2->next->next = new ListNode(3);
    head2->next->next->next = new ListNode(4);
    head2->next->next->next->next = new ListNode(5);

    ListNode* reordered2 = sol.reorder(head2);
    vector<int> expected2 = {1, 5, 2, 4, 3};
    assert(sol.getListValues(reordered2) == expected2);

    // Test case 3: Short list [1, 2]
    // Expected result: [1, 2]
    ListNode* head3 = new ListNode(1);
    head3->next = new ListNode(2);

    ListNode* reordered3 = sol.reorder(head3);
    vector<int> expected3 = {1, 2};
    assert(sol.getListValues(reordered3) == expected3);

    // Test case 4: Single node [1]
    // Expected result: [1]
    ListNode* head4 = new ListNode(1);

    ListNode* reordered4 = sol.reorder(head4);
    vector<int> expected4 = {1};
    assert(sol.getListValues(reordered4) == expected4);

    cout << "All test cases passed." << endl;

    // Clean up memory
    for (ListNode* curr = head1; curr != nullptr;) {
        ListNode* temp = curr;
        curr = curr->next;
        delete temp;
    }
    for (ListNode* curr = head2; curr != nullptr;) {
        ListNode* temp = curr;
        curr = curr->next;
        delete temp;
    }
    for (ListNode* curr = head3; curr != nullptr;) {
        ListNode* temp = curr;
        curr = curr->next;
        delete temp;
    }
    for (ListNode* curr = head4; curr != nullptr;) {
        ListNode* temp = curr;
        curr = curr->next;
        delete temp;
    }

    return 0;
}
