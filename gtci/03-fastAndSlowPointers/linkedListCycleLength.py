class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


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


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(linkedListCycleLength(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(linkedListCycleLength(head)))


main()
