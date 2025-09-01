class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def calculateLengthOfCycle(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if fast is None or fast.next is None:
            return -1  # no cycle

        cycle_length = 1
        itr = slow.next
        while itr != slow:
            cycle_length += 1
            itr = itr.next

        return cycle_length


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = head.next  # create a cycle

    sol = Solution()
    assert sol.calculateLengthOfCycle(head) == 3

    print("All test cases passed.")
