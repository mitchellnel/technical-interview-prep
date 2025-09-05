class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head):
        stack = []

        curr = head
        while curr is not None:
            while len(stack) > 0 and curr.val > stack[-1].val:
                stack.pop()

            stack.append(curr)
            curr = curr.next

        prev = None
        while len(stack) > 0:
            node = stack.pop()
            node.next = prev
            prev = node

        return prev


def get_linked_list_values(head):
    values = []
    curr = head
    while curr is not None:
        values.append(curr.val)
        curr = curr.next
    return values


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Regular case with multiple removals
    # Input: 5->2->13->3->8
    # Output: 13->8 (5,2 removed because 13 is greater, 3 removed because 8 is greater)
    head = Node(5)
    head.next = Node(2)
    head.next.next = Node(13)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(8)

    result = sol.removeNodes(head)
    values = get_linked_list_values(result)
    assert values == [13, 8], f"Test Case 1 Failed: Expected [13, 8], but got {values}"

    # Test Case 2: Monotonically increasing list (no removals)
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    result = sol.removeNodes(head)
    values = get_linked_list_values(result)
    assert values == [4], f"Test Case 2 Failed: Expected [4], but got {values}"

    # Test Case 3: Monotonically decreasing list (only last node remains)
    head = Node(4)
    head.next = Node(3)
    head.next.next = Node(2)
    head.next.next.next = Node(1)

    result = sol.removeNodes(head)
    values = get_linked_list_values(result)
    assert values == [
        4,
        3,
        2,
        1,
    ], f"Test Case 3 Failed: Expected [4, 3, 2, 1], but got {values}"

    # Test Case 4: All equal values (no removals)
    head = Node(5)
    head.next = Node(5)
    head.next.next = Node(5)

    result = sol.removeNodes(head)
    values = get_linked_list_values(result)
    assert values == [
        5,
        5,
        5,
    ], f"Test Case 4 Failed: Expected [5, 5, 5], but got {values}"

    # Test Case 5: Single node
    head = Node(1)

    result = sol.removeNodes(head)
    values = get_linked_list_values(result)
    assert values == [1], f"Test Case 5 Failed: Expected [1], but got {values}"

    # Test Case 6: Empty list
    result = sol.removeNodes(None)
    assert result is None, "Test Case 6 Failed: Empty list should return None"

    # Test Case 7: Alternating values
    # Input: 1->3->2->4->3->5
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(2)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(3)
    head.next.next.next.next.next = Node(5)

    result = sol.removeNodes(head)
    values = get_linked_list_values(result)
    assert values == [5], f"Test Case 7 Failed: Expected [3, 4, 5], but got {values}"

    print("All test cases passed.")
