#include <cassert>
#include <iostream>

#include "linked_list_utils.h"

using namespace std;

class Solution {
   public:
    ListNode* rotate(ListNode* head, int rotations) {
        if (head == nullptr || head->next == nullptr) return head;

        const int linkedListLength = Solution::getLinkedListLength(head);
        rotations = rotations % linkedListLength;

        if (rotations == 0) return head;

        const int indexOfFirstNodeInRotateSublist =
            linkedListLength - rotations;

        // seek to the first node in the rotate sublist
        ListNode* prev = nullptr;
        ListNode* curr = head;
        int i = 0;
        while (curr != nullptr && i < indexOfFirstNodeInRotateSublist) {
            prev = curr;
            curr = curr->next;

            i++;
        }

        // record the node before the rotate sublist, and the first node of the
        // rotate sublist
        ListNode* lastNodeBeforeRotateSublist = prev;
        ListNode* firstNodeOfRotateSublist = curr;

        // seek to the end of the rotate sublist
        i = 0;
        while (curr != nullptr &&
               i < linkedListLength - indexOfFirstNodeInRotateSublist - 1) {
            prev = curr;
            curr = curr->next;

            i++;
        }

        // perform the rotation
        lastNodeBeforeRotateSublist->next = nullptr;
        curr->next = head;
        head = firstNodeOfRotateSublist;

        return head;
    }

   private:
    static int getLinkedListLength(ListNode* head) {
        int length = 0;
        ListNode* curr = head;

        while (curr != nullptr) {
            curr = curr->next;
            length++;
        }

        return length;
    }
};

int main() {
    Solution sol;

    // Test Case 1: Normal rotation
    // Input: 1->2->3->4->5, rotations = 2
    // Output: 4->5->1->2->3
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);
        head->next->next = new ListNode(3);
        head->next->next->next = new ListNode(4);
        head->next->next->next->next = new ListNode(5);

        ListNode* result = sol.rotate(head, 2);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {4, 5, 1, 2, 3};

        assert(values == expected &&
               "Test Case 1 Failed: List not rotated correctly");
        cleanupLinkedList(result);
    }

    // Test Case 2: Rotation equal to length (should be same as input)
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);
        head->next->next = new ListNode(3);

        ListNode* result = sol.rotate(head, 3);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {1, 2, 3};

        assert(values == expected &&
               "Test Case 2 Failed: Full rotation should return original list");
        cleanupLinkedList(result);
    }

    // Test Case 3: Rotation greater than length
    // rotations = 5 for list length 3 should be same as rotations = 2
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);
        head->next->next = new ListNode(3);

        ListNode* result = sol.rotate(head, 5);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {2, 3, 1};

        assert(values == expected &&
               "Test Case 3 Failed: Modulo rotation not working correctly");
        cleanupLinkedList(result);
    }

    // Test Case 4: Single node
    {
        ListNode* head = new ListNode(1);

        ListNode* result = sol.rotate(head, 1);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {1};

        assert(values == expected &&
               "Test Case 4 Failed: Single node should remain unchanged");
        cleanupLinkedList(result);
    }

    // Test Case 5: Empty list
    {
        ListNode* result = sol.rotate(nullptr, 1);
        assert(result == nullptr &&
               "Test Case 5 Failed: Empty list should return nullptr");
    }

    // Test Case 6: Zero rotations
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);
        head->next->next = new ListNode(3);

        ListNode* result = sol.rotate(head, 0);
        vector<int> values = getLinkedListValues(result);
        vector<int> expected = {1, 2, 3};

        assert(values == expected &&
               "Test Case 6 Failed: Zero rotations should not change list");
        cleanupLinkedList(result);
    }

    // Test Case 7: Large number of rotations
    {
        ListNode* head = new ListNode(1);
        head->next = new ListNode(2);
        head->next->next = new ListNode(3);

        ListNode* result = sol.rotate(head, 1000000);
        vector<int> values = getLinkedListValues(result);
        // 1000000 % 3 = 1, so rotate by 1
        vector<int> expected = {3, 1, 2};

        assert(values == expected &&
               "Test Case 8 Failed: Large rotation not handled correctly");
        cleanupLinkedList(result);
    }

    cout << "All test cases passed." << endl;
    return 0;
}
