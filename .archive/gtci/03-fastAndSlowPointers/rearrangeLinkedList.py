class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end="")
            temp = temp.next
        print()


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


def rearrangeLinkedList(head):
    if head is None or head.next is None:
        return head

    # find the middle of the linked list
    middle = middleOfLinkedList(head)

    # reverse the second half of the linked list
    head_second_half = reverseLinkedList(middle)

    head_first_half = head

    # traverse both halves and alternately insert
    while head_first_half is not None and head_second_half is not None:
        temp = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = temp

        temp = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = temp

    # set the next of the last node to None
    if head_first_half is not None:
        head_first_half.next = None

    return head


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    rearrangeLinkedList(head)
    head.print_list()


main()
