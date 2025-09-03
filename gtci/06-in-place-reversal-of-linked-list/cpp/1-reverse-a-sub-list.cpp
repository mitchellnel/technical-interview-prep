using namespace std;

#include <cassert>
#include <iostream>

#include "linked_list_utils.h"

class Solution {
   public:
    ListNode* reverse(ListNode* head, int p, int q) {
        if (head == nullptr || p == q) return head;

        ListNode* prev = nullptr;
        ListNode* curr = head;
        int i = 1;

        // seek to p
        while (curr != nullptr && i < p) {
            prev = curr;
            curr = curr->next;

            i++;
        }

        // record the last node before the sublist, and the first node of the
        // sublist
        ListNode* lastNodeOfSublist = prev;
        ListNode* firstNodeOfSublist = curr;

        // reverse the sublist
        prev = nullptr;
        while (curr != nullptr && i < q + 1) {
            ListNode* temp = curr->next;

            curr->next = prev;
            prev = curr;

            curr = temp;

            i++;
        }

        // connect the first node of the reversed sublist (q) to the rest of the
        // list
        if (lastNodeOfSublist != nullptr)
            lastNodeOfSublist->next = prev;
        else
            head = prev;

        // connect the last node of the reversed sublist (p) to the rest of the
        // list
        firstNodeOfSublist->next = curr;

        return head;
    }
};

int main() {
    Solution sol;

    // Test Case 1: Normal case - reverse middle portion
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);
        head->next->next = new ListNode(3);
        head->next->next->next = new ListNode(4);
        head->next->next->next->next = new ListNode(5);

        ListNode* result = sol.reverse(head, 2, 4);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {1, 4, 3, 2, 5};

        assert(values == expected &&
               "Test Case 1 Failed: Middle portion not reversed correctly");
        cleanupLinkedList(result);
    }

    // Test Case 2: Reverse entire list
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);
        head->next->next = new ListNode(3);

        ListNode* result = sol.reverse(head, 1, 3);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {3, 2, 1};

        assert(values == expected &&
               "Test Case 2 Failed: Complete list reversal failed");
        cleanupLinkedList(result);
    }

    // Test Case 3: Single node between p and q
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);
        head->next->next = new ListNode(3);

        ListNode* result = sol.reverse(head, 2, 2);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {1, 2, 3};

        assert(
            values == expected &&
            "Test Case 3 Failed: Single node reversal should not change list");
        cleanupLinkedList(result);
    }

    // Test Case 4: Empty list
    {
        ListNode* result = sol.reverse(nullptr, 1, 2);
        assert(result == nullptr &&
               "Test Case 4 Failed: Empty list should return nullptr");
    }

    // Test Case 5: Reverse at list boundaries
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);
        head->next->next = new ListNode(3);
        head->next->next->next = new ListNode(4);

        ListNode* result = sol.reverse(head, 1, 2);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {2, 1, 3, 4};

        assert(values == expected &&
               "Test Case 5 Failed: Start of list reversal failed");
        cleanupLinkedList(result);
    }

    cout << "All test cases passed." << endl;
    return 0;
}
