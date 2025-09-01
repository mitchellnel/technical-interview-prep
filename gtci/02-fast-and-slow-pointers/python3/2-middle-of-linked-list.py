class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def findMiddle(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    sol = Solution()
    assert sol.findMiddle(head).val == 3

    head.next.next.next.next.next = Node(6)
    assert sol.findMiddle(head).val == 4

    print("All test cases passed.")
