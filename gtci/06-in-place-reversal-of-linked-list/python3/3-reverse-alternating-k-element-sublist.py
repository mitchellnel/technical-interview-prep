class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def reverse(self, head, k):
        prev = None
        curr = head

        reverse_sublist = True
        while curr:
            if reverse_sublist:
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
            else:
                # seek k nodes
                i = 0
                while curr and i < k:
                    prev = curr
                    curr = curr.next

                    i += 1

            reverse_sublist = not reverse_sublist

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

    # Test Case 1: Normal case with k=2 (should reverse alternating pairs)
    # Input: 1->2->3->4->5->6->7->8
    # Output: 2->1->3->4->6->5->7->8 (reverse pairs at positions 1-2, 5-6)
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    result = sol.reverse(head, k=2)
    values = get_linked_list_values(result)
    assert values == [
        2,
        1,
        3,
        4,
        6,
        5,
        7,
        8,
    ], f"Test Case 1 Failed: Expected [2, 1, 3, 4, 6, 5, 7, 8], but got {values}"

    # Test Case 2: List length is not divisible by k, and last part is to be reversed
    # Should reverse the last part even though it is not k-length
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
    assert values == [3, 2, 1, 4, 5, 6, 8, 7]

    # Test Case 2: k equals to list length
    # Should reverse first k elements, keep next k elements as is
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    result = sol.reverse(head, k=3)
    values = get_linked_list_values(result)
    assert values == [
        3,
        2,
        1,
        4,
        5,
        6,
    ], f"Test Case 2 Failed: Expected [3, 2, 1, 4, 5, 6], but got {values}"

    # Test Case 3: k greater than list length
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    result = sol.reverse(head, k=4)
    values = get_linked_list_values(result)
    assert values == [
        3,
        2,
        1,
    ], f"Test Case 3 Failed: Expected [3, 2, 1], but got {values}"

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
    head.next.next.next = Node(4)

    result = sol.reverse(head, k=1)
    values = get_linked_list_values(result)
    assert values == [
        1,
        2,
        3,
        4,
    ], f"Test Case 6 Failed: Expected [1, 2, 3, 4], but got {values}"

    # Test Case 7: Odd number of elements with k=2
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
        3,
        4,
        5,
    ], f"Test Case 7 Failed: Expected [2, 1, 3, 4, 5], but got {values}"

    print("All test cases passed.")
