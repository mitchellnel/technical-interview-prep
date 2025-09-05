#include <cassert>
#include <iostream>
#include <stack>
#include <vector>

#include "linked_list_utils.h"

using std::cout;
using std::endl;
using std::vector;

class Solution {
   public:
    ListNode* removeNodes(ListNode* head) {
        std::stack<ListNode*> nodeStack;

        ListNode* curr = head;
        while (curr != nullptr) {
            while (nodeStack.size() > 0 && curr->val > nodeStack.top()->val)
                nodeStack.pop();

            nodeStack.push(curr);
            curr = curr->next;
        }

        ListNode* prev = nullptr;
        while (nodeStack.size() > 0) {
            ListNode* node = nodeStack.top();
            nodeStack.pop();

            node->next = prev;
            prev = node;
        }

        return prev;
    }
};

int main() {
    Solution sol;

    // Test Case 1: Regular case with multiple removals
    // Input: 5->2->13->3->8
    // Output: 13->8 (5,2 removed because 13 is greater, 3 removed because 8 is
    // greater)
    {
        ListNode* head = new ListNode(5);
        head->next = new ListNode(2);
        head->next->next = new ListNode(13);
        head->next->next->next = new ListNode(3);
        head->next->next->next->next = new ListNode(8);

        ListNode* result = sol.removeNodes(head);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {13, 8};

        assert(values == expected &&
               "Test Case 1 Failed: Multiple nodes not removed correctly");
        cleanupLinkedList(result);
    }

    // Test Case 3: Monotonically decreasing list
    {
        ListNode* head = new ListNode(4);
        head->next = new ListNode(3);
        head->next->next = new ListNode(2);
        head->next->next->next = new ListNode(1);

        ListNode* result = sol.removeNodes(head);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {4, 3, 2, 1};

        assert(values == expected &&
               "Test Case 3 Failed: Decreasing list should keep all nodes");
        cleanupLinkedList(result);
    }

    // Test Case 4: All equal values (no removals)
    {
        ListNode* head = new ListNode(5);
        head->next = new ListNode(5);
        head->next->next = new ListNode(5);

        ListNode* result = sol.removeNodes(head);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {5, 5, 5};

        assert(values == expected &&
               "Test Case 4 Failed: Equal values should all remain");
        cleanupLinkedList(result);
    }

    // Test Case 5: Single node
    {
        ListNode* head = new ListNode(1);

        ListNode* result = sol.removeNodes(head);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {1};

        assert(values == expected &&
               "Test Case 5 Failed: Single node should remain unchanged");
        cleanupLinkedList(result);
    }

    // Test Case 6: Empty list
    {
        ListNode* result = sol.removeNodes(nullptr);
        assert(result == nullptr &&
               "Test Case 6 Failed: Empty list should return nullptr");
    }

    // Test Case 7: Alternating values
    // Input: 1->3->2->4->3->5
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(3);
        head->next->next = new ListNode(2);
        head->next->next->next = new ListNode(4);
        head->next->next->next->next = new ListNode(3);
        head->next->next->next->next->next = new ListNode(5);

        ListNode* result = sol.removeNodes(head);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {5};

        assert(values == expected &&
               "Test Case 7 Failed: Complex alternating pattern not handled "
               "correctly");
        cleanupLinkedList(result);
    }

    cout << "All test cases passed." << endl;
    return 0;
}
