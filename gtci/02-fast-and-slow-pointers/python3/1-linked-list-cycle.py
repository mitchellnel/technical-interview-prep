class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = head.next  # create a cycle

    sol = Solution()
    assert sol.hasCycle(head) == True

    print("All test cases passed.")
