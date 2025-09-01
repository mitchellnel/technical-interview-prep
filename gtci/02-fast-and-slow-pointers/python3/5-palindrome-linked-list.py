class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:
    def isPalindrome(self, head):
        middle = self.get_middle_node(head)

        end = self.reverse_list(middle)

        l1 = head
        l2 = end
        while l1 is not None and l2 is not None:
            if l1.val != l2.val:
                return False

            l1 = l1.next
            l2 = l2.next

        self.reverse_list(end)

        return True

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
            temp = curr.next

            curr.next = prev
            prev = curr
            curr = temp

        return prev


if __name__ == "__main__":
    sol = Solution()

    head = Node(1, Node(2, Node(3, Node(2, Node(1)))))
    head2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    head3 = Node(1, Node(2, Node(2, Node(1))))

    assert sol.isPalindrome(head) == True
    assert sol.isPalindrome(head2) == False
    assert sol.isPalindrome(head3) == True

    print("All test cases passed.")
