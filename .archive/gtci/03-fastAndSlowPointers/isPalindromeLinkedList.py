class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def middleOfLinkedList(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def reverseLinkedList(head):
    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next

    return prev


def isPalindromeLinkedList(head):
    if head is None or head.next is None:
        return True

    # find the middle of the linked list
    middle = middleOfLinkedList(head)

    # reverse the second half of the linked list
    head_second_half = reverseLinkedList(middle)

    # copy haed of reversed part to revert back to later
    copy_head_second_half = head_second_half

    # compare the first and the second half
    while head is not None and head_second_half is not None:
        if head.value != head_second_half.value:
            return False

        head = head.next
        head_second_half = head_second_half.next

    # revert the reverse of the second half
    reverseLinkedList(copy_head_second_half)

    return head is None and head_second_half is None


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(isPalindromeLinkedList(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(isPalindromeLinkedList(head)))


main()
