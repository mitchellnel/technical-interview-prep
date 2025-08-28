class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end="")
            temp = temp.next
        print()


def linkedListCycleLength(head):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            break

    cycle_length = 1
    curr = slow.next
    while curr != slow:
        cycle_length += 1
        curr = curr.next

    return cycle_length


def startOfLinkedListCycle(head):
    linked_list_length = linkedListCycleLength(head)

    ptr1, ptr2 = head, head

    # move ptr2 forward by linked_list_length nodes
    for _ in range(linked_list_length):
        ptr2 = ptr2.next

    # traverse with both pointers until they meet
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(startOfLinkedListCycle(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(startOfLinkedListCycle(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(startOfLinkedListCycle(head).value))


main()
