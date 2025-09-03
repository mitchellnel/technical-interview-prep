class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def rotate(self, head, rotations):
        if head is None or head.next is None:
            return head

        linked_list_length = self.get_linked_list_length(head)
        rotations = rotations % linked_list_length

        if rotations == 0:
            return head

        first_node_to_rotate_idx = linked_list_length - rotations

        # seek to the first node to rotate
        i = 0
        prev = None
        curr = head
        while curr and i < first_node_to_rotate_idx:
            prev = curr
            curr = curr.next

            i += 1

        last_node_before_rotate_sublist = prev
        first_node_of_rotate_sublist = curr

        # seek to the end of the rotate sublist
        i = 0
        while curr and i < linked_list_length - first_node_to_rotate_idx - 1:
            prev = curr
            curr = curr.next

            i += 1

        # make the rotation
        last_node_before_rotate_sublist.next = None
        curr.next = head
        head = first_node_of_rotate_sublist

        return head

    def get_linked_list_length(self, head):
        length = 0
        curr = head

        while curr:
            curr = curr.next
            length += 1

        return length


def get_linked_list_values(head):
    values = []
    curr = head
    while curr is not None:
        values.append(curr.val)
        curr = curr.next
    return values


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Normal rotation
    # Input: 1->2->3->4->5, rotations = 2
    # Output: 4->5->1->2->3
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    result = sol.rotate(head, rotations=2)
    values = get_linked_list_values(result)
    assert values == [
        4,
        5,
        1,
        2,
        3,
    ], f"Test Case 1 Failed: Expected [4, 5, 1, 2, 3], but got {values}"

    # Test Case 2: Rotation equal to length (should be same as input)
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    result = sol.rotate(head, rotations=3)
    values = get_linked_list_values(result)
    assert values == [
        1,
        2,
        3,
    ], f"Test Case 2 Failed: Expected [1, 2, 3], but got {values}"

    # Test Case 3: Rotation greater than length
    # rotations = 5 for list length 3 should be same as rotations = 2
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    result = sol.rotate(head, rotations=5)
    values = get_linked_list_values(result)
    assert values == [
        2,
        3,
        1,
    ], f"Test Case 3 Failed: Expected [2, 3, 1], but got {values}"

    # Test Case 4: Single node
    head = Node(1)

    result = sol.rotate(head, rotations=1)
    values = get_linked_list_values(result)
    assert values == [1], f"Test Case 4 Failed: Expected [1], but got {values}"

    # Test Case 5: Empty list
    result = sol.rotate(None, rotations=1)
    assert result is None, "Test Case 5 Failed: Empty list should return None"

    # Test Case 6: Zero rotations
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    result = sol.rotate(head, rotations=0)
    values = get_linked_list_values(result)
    assert values == [
        1,
        2,
        3,
    ], f"Test Case 6 Failed: Expected [1, 2, 3], but got {values}"

    # Test Case 7: Large number of rotations
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    result = sol.rotate(head, rotations=1000000)
    values = get_linked_list_values(result)
    # 1000000 % 3 = 1, so rotate by 1
    assert values == [
        3,
        1,
        2,
    ], f"Test Case 8 Failed: Expected [3, 1, 2], but got {values}"

    print("All test cases passed.")
