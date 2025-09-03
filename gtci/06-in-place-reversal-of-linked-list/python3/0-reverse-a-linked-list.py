class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def reverse(self, head):
        prev = None
        curr = head

        while curr is not None:
            temp = curr.next

            curr.next = prev
            prev = curr

            curr = temp

        return prev


if __name__ == "__main__":
    from util import get_linked_list_values

    # Test case 1: Multiple nodes (1->2->3 should become 3->2->1)
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    sol = Solution()
    reversed_head = sol.reverse(head)
    result = get_linked_list_values(reversed_head)
    assert result == [3, 2, 1], f"Expected [3, 2, 1], but got {result}"

    # Test case 2: Single node (should remain the same)
    single_node = Node(5)
    reversed_single = sol.reverse(single_node)
    result = get_linked_list_values(reversed_single)
    assert result == [5], f"Expected [5], but got {result}"

    # Test case 3: Empty list (None should remain None)
    empty_list = None
    reversed_empty = sol.reverse(empty_list)
    assert reversed_empty is None, "Expected None for empty list"

    print("All test cases passed.")
