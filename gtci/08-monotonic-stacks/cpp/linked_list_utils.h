#ifndef LINKED_LIST_UTILS_H
#define LINKED_LIST_UTILS_H

#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int val) : val(val), next(nullptr) {}
};

inline std::vector<int> getLinkedListValues(ListNode* head) {
    std::vector<int> values;
    ListNode* curr = head;
    while (curr != nullptr) {
        values.push_back(curr->val);
        curr = curr->next;
    }
    return values;
}

inline void cleanupLinkedList(ListNode* head) {
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

#endif  // LINKED_LIST_UTILS_H
