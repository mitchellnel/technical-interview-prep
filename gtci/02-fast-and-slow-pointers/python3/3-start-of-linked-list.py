class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def findCycleStart(self, head):
        slow = head
        fast = head
        cycle_length = None
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                cycle_length = self.calculateLengthOfCycle(slow, fast)
                break

        print(cycle_length)

        slow = head
        fast = head
        while cycle_length > 0:
            fast = fast.next
            cycle_length -= 1

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

    def calculateLengthOfCycle(self, cycle_start):
        cycle_length = 1
        itr = cycle_start.next
        while itr != cycle_start:
            cycle_length += 1
            itr = itr.next

        return cycle_length


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next

    sol = Solution()
    assert sol.findCycleStart(head).val == 2

    print("All test cases passed.")
