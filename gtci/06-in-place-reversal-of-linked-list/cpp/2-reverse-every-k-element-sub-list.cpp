#include <cassert>
#include <iostream>

#include "linked_list_utils.h"

using namespace std;

class Solution {
   public:
    ListNode* reverse(ListNode* head, int k) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr != nullptr) {
            int i = 0;

            ListNode* lastNodeBeforeSublist = prev;
            ListNode* firstNodeOfSublist = curr;
            while (curr != nullptr && i < k) {
                ListNode* temp = curr->next;

                curr->next = prev;
                prev = curr;

                curr = temp;

                i++;
            }

            if (lastNodeBeforeSublist != nullptr)
                lastNodeBeforeSublist->next = prev;
            else
                head = prev;

            firstNodeOfSublist->next = curr;

            prev = firstNodeOfSublist;
        }

        return head;
    }
};

int main() {
    Solution sol;

    // Test Case 1: Normal case with k=2 (should reverse in pairs)
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);
        head->next->next = new ListNode(3);
        head->next->next->next = new ListNode(4);
        head->next->next->next->next = new ListNode(5);

        ListNode* result = sol.reverse(head, 2);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {2, 1, 4, 3, 5};

        assert(values == expected &&
               "Test Case 1 Failed: List not correctly reversed in pairs");
        cleanupLinkedList(result);
    }

    // Test Case 2: List length is not divisible by k
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);
        head->next->next = new ListNode(3);
        head->next->next->next = new ListNode(4);
        head->next->next->next->next = new ListNode(5);
        head->next->next->next->next->next = new ListNode(6);
        head->next->next->next->next->next->next = new ListNode(7);
        head->next->next->next->next->next->next->next = new ListNode(8);

        ListNode* result = sol.reverse(head, 3);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {3, 2, 1, 6, 5, 4, 8, 7};

        assert(values == expected &&
               "Test Case 1 Failed: List not correctly reversed in pairs");
        cleanupLinkedList(result);
    }

    // Test Case 2: k equals to list length
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);
        head->next->next = new ListNode(3);

        ListNode* result = sol.reverse(head, 3);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {3, 2, 1};

        assert(values == expected &&
               "Test Case 2 Failed: Complete list reversal failed");
        cleanupLinkedList(result);
    }

    // Test Case 3: k greater than list length
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);

        ListNode* result = sol.reverse(head, 3);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {2, 1};

        assert(values == expected &&
               "Test Case 3 Failed: List should be fully reversed when k > "
               "length");
        cleanupLinkedList(result);
    }

    // Test Case 4: Single node
    {
        ListNode* head = new ListNode(1);

        ListNode* result = sol.reverse(head, 2);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {1};

        assert(values == expected &&
               "Test Case 4 Failed: Single node should remain unchanged");
        cleanupLinkedList(result);
    }

    // Test Case 5: Empty list
    {
        ListNode* result = sol.reverse(nullptr, 2);
        assert(result == nullptr &&
               "Test Case 5 Failed: Empty list should return nullptr");
    }

    // Test Case 6: k=1 (no reversal should occur)
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);
        head->next->next = new ListNode(3);

        ListNode* result = sol.reverse(head, 1);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {1, 2, 3};

        assert(values == expected &&
               "Test Case 6 Failed: k=1 should not change the list");
        cleanupLinkedList(result);
    }

    cout << "All test cases passed." << endl;
    return 0;
}
