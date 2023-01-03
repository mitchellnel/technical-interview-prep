# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = None
        current = None
        while list1 != None and list2 != None:
            print(f"list1 is {list1.val}, list2 is {list2.val}")
            if list1.val <= list2.val:
                if head is None:
                    head = list1
                    current = list1
                else:
                    current.next = list1
                    print(f"current before: {current}")
                    current = current.next if current.next is not None else current
                    print(f"current after: {current}")

                list1 = list1.next
            else:
                if head is None:
                    head = list2
                    current = list2
                else:
                    current.next = list2
                    print(f"current before: {current}")
                    current = current.next if current.next is not None else current
                    print(f"current after: {current}")

                list2 = list2.next

        # append final parts of the list
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            print(f"fdjs {list2}")
            current.next = list2

        return head
