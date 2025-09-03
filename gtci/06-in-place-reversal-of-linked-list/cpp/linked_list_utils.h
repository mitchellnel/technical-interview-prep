#ifndef LINKED_LIST_UTILS_H
#define LINKED_LIST_UTILS_H

#include <vector>

class ListNode {
   public:
    int val = 0;
    ListNode* next;

    ListNode(int value) {
        this->val = value;
        next = nullptr;
    }
};

// Helper function to convert linked list to vector for easier assertion
inline std::vector<int> getLinkedListValues(ListNode* head) {
    std::vector<int> values;
    ListNode* curr = head;
    while (curr != nullptr) {
        values.push_back(curr->val);
        curr = curr->next;
    }
    return values;
}

// Helper function to free memory
inline void cleanupLinkedList(ListNode* head) {
    ListNode* current = head;
    while (current != nullptr) {
        ListNode* temp = current;
        current = current->next;
        delete temp;
    }
}

#endif  // LINKED_LIST_UTILS_H
