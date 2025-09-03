class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def reverse(self, head, p, q):
        if head is None or p == q:
            return head

        prev = None
        curr = head

        # seek to p
        i = 1
        while curr and i != p:
            prev = curr
            curr = curr.next

            i += 1

        # keep track of the last node before the sublist, and the first node of the sublist
        last_node_before_sublist = prev
        first_node_of_sublist = curr

        # reverse from p to just before q
        prev = None
        while curr and i != q + 1:
            temp = curr.next

            curr.next = prev
            prev = curr

            curr = temp

            i += 1

        # now connect the last node before the sublist to q
        if last_node_before_sublist:
            last_node_before_sublist.next = prev
        else:
            head = prev

        # and now connect the first node in the sublist to the rest of the list
        first_node_of_sublist.next = curr

        return head


if __name__ == "__main__":
    from util import get_linked_list_values

    # Test case 1: Reverse sublist (1->2->3->4->5, p=2, q=4 should become 1->5->4->3->2)
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    sol = Solution()
    reversed_head = sol.reverse(head, 2, 4)
    result = get_linked_list_values(reversed_head)
    assert result == [1, 4, 3, 2, 5], f"Expected [1, 4, 3, 2, 5], but got {result}"

    # Test case 2: Reverse entire list (1->2->3 should become 3->2->1)
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    reversed_head = sol.reverse(head, 1, 3)
    result = get_linked_list_values(reversed_head)
    assert result == [3, 2, 1], f"Expected [3, 2, 1], but got {result}"

    # Test case 3: Reverse single element (2->1 should become 1->2)
    head = Node(1)
    head.next = Node(2)

    reversed_head = sol.reverse(head, 1, 1)
    result = get_linked_list_values(reversed_head)
    assert result == [1, 2], f"Expected [1, 2], but got {result}"

    print("All test cases passed.")
