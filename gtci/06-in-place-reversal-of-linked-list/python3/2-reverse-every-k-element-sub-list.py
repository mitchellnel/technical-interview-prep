class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def reverse(self, head, k):
        prev = None
        curr = head

        while curr:
            i = 0
            last_node_before_sublist = prev
            first_node_of_sublist = curr
            while curr and i < k:
                temp = curr.next

                curr.next = prev
                prev = curr

                curr = temp

                i += 1

            if last_node_before_sublist:
                last_node_before_sublist.next = prev
            else:
                head = prev

            first_node_of_sublist.next = curr

            prev = first_node_of_sublist

        return head


def get_linked_list_values(head):
    values = []
    curr = head
    while curr is not None:
        values.append(curr.val)
        curr = curr.next
    return values


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Normal case with k=2 (should reverse in pairs)
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    result = sol.reverse(head, k=2)
    values = get_linked_list_values(result)
    assert values == [
        2,
        1,
        4,
        3,
        5,
    ], f"Test Case 1 Failed: Expected [2, 1, 4, 3, 5], but got {values}"

    # Test Case 2: List length is not divisible by k
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    result = sol.reverse(head, k=3)
    values = get_linked_list_values(result)
    assert values == [3, 2, 1, 6, 5, 4, 8, 7]

    # Test Case 2: k equals to list length
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    result = sol.reverse(head, k=3)
    values = get_linked_list_values(result)
    assert values == [
        3,
        2,
        1,
    ], f"Test Case 2 Failed: Expected [3, 2, 1], but got {values}"

    # Test Case 3: k greater than list length
    head = Node(1)
    head.next = Node(2)

    result = sol.reverse(head, k=3)
    values = get_linked_list_values(result)
    assert values == [2, 1], f"Test Case 3 Failed: Expected [2, 1], but got {values}"

    # Test Case 4: Single node
    head = Node(1)

    result = sol.reverse(head, k=2)
    values = get_linked_list_values(result)
    assert values == [1], f"Test Case 4 Failed: Expected [1], but got {values}"

    # Test Case 5: Empty list
    result = sol.reverse(None, k=2)
    assert result is None, "Test Case 5 Failed: Empty list should return None"

    # Test Case 6: k=1 (no reversal should occur)
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    result = sol.reverse(head, k=1)
    values = get_linked_list_values(result)
    assert values == [
        1,
        2,
        3,
    ], f"Test Case 6 Failed: Expected [1, 2, 3], but got {values}"

    print("All test cases passed.")
