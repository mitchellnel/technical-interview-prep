class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def reorder(self, head):
        middle = self.get_middle_node(head)

        first_half_curr = head
        second_half_curr = self.reverse_list(middle)

        while first_half_curr is not None and second_half_curr is not None:
            temp = first_half_curr.next

            first_half_curr.next = second_half_curr
            first_half_curr = temp

            temp = second_half_curr.next

            second_half_curr.next = first_half_curr
            second_half_curr = temp

        if first_half_curr is not None:
            first_half_curr.next = None

        return head

    def get_middle_node(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse_list(self, head):
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def get_list_values(self, head):
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values


if __name__ == "__main__":
    # Test case 1: Even length list [1, 2, 3, 4]
    # Expected result: [1, 4, 2, 3]
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)

    sol = Solution()
    reordered1 = sol.reorder(head1)
    assert sol.get_list_values(reordered1) == [1, 4, 2, 3], "Test case 1 failed"

    # Test case 2: Odd length list [1, 2, 3, 4, 5]
    # Expected result: [1, 5, 2, 4, 3]
    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = Node(3)
    head2.next.next.next = Node(4)
    head2.next.next.next.next = Node(5)

    reordered2 = sol.reorder(head2)
    assert sol.get_list_values(reordered2) == [1, 5, 2, 4, 3], "Test case 2 failed"

    # Test case 3: Short list [1, 2]
    # Expected result: [1, 2]
    head3 = Node(1)
    head3.next = Node(2)

    reordered3 = sol.reorder(head3)
    assert sol.get_list_values(reordered3) == [1, 2], "Test case 3 failed"

    # Test case 4: Single node [1]
    # Expected result: [1]
    head4 = Node(1)

    reordered4 = sol.reorder(head4)
    assert sol.get_list_values(reordered4) == [1], "Test case 4 failed"

    print("All test cases passed.")
