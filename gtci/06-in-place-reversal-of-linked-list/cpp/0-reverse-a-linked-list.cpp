#include <cassert>
#include <iostream>

#include "linked_list_utils.h"

using namespace std;

class Solution {
   public:
    ListNode* reverse(ListNode* head) {
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
    bool allTestsPassed = true;

    // Test Case 1: Multiple nodes (1->2->3 should become 3->2->1)
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);
        head->next->next = new ListNode(3);

        ListNode* reversed = sol.reverse(head);
        vector<int> result = getLinkedListValues(reversed);
        vector<int> expected = {3, 2, 1};

        assert(result == expected &&
               "Test Case 1 Failed: Multiple nodes not reversed correctly");
        cleanupLinkedList(reversed);
    }

    // Test Case 2: Single node (should remain the same)
    {
        ListNode* singleNode = new ListNode(5);
        ListNode* reversed = sol.reverse(singleNode);
        vector<int> result = getLinkedListValues(reversed);
        vector<int> expected = {5};

        assert(result == expected &&
               "Test Case 2 Failed: Single node case failed");
        cleanupLinkedList(reversed);
    }

    // Test Case 3: Empty list (nullptr should remain nullptr)
    {
        ListNode* emptyList = nullptr;
        ListNode* reversed = sol.reverse(emptyList);
        assert(reversed == nullptr &&
               "Test Case 3 Failed: Empty list should return nullptr");
    }

    cout << "All test cases passed." << endl;
    return 0;
}
