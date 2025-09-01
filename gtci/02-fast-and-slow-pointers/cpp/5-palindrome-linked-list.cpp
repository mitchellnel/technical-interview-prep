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

    ListNode(int value, ListNode* next) {
        this->val = value;
        this->next = next;
    }
};

class Solution {
   public:
    bool isPalindrome(ListNode* head) {
        ListNode* middle = Solution::getMiddleNode(head);

        ListNode* firstHalfStart = Solution::reverseList(head);
        ListNode* secondHalfStart = Solution::reverseList(middle);

        while (firstHalfStart != nullptr and secondHalfStart != nullptr) {
            if (firstHalfStart->val != secondHalfStart->val) return false;

            firstHalfStart = firstHalfStart->next;
            secondHalfStart = secondHalfStart->next;
        }

        Solution::reverseList(secondHalfStart);

        return true;
    }

   private:
    static ListNode* getMiddleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        return slow;
    }

    static ListNode* reverseList(ListNode* head) {
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
    Solution sol;

    ListNode* head = new ListNode(
        1, new ListNode(2, new ListNode(3, new ListNode(2, new ListNode(1)))));
    ListNode* head2 = new ListNode(
        1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
    ListNode* head3 =
        new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(1))));

    assert(sol.isPalindrome(head) == true);
    assert(sol.isPalindrome(head2) == false);
    assert(sol.isPalindrome(head3) == true);

    cout << "All test cases passed." << endl;

    // Clean up memory
    for (ListNode* curr = head; curr != nullptr;) {
        ListNode* temp = curr;
        curr = curr->next;
        delete temp;
    }

    return 0;
}
