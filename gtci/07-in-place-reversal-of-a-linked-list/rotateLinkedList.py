class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def rotate_list(head, rotate_amount):
    if rotate_amount <= 0 or head is None or head.next is None:
        return head

    current = head
    previous = None

    # get length of the list
    list_length = 0  # starts at 1 because current is head
    while current is not None:
        previous = current
        current = current.next
        list_length += 1

    rotate_amount %= list_length

    # the last node's next pointer will be to the head of the list
    previous.next = head

    # we need to traverse to the node before the node before our new head
    #   (this is list_length - rotate_amount - 1)
    # then we will set the next pointer of this node to null
    current = head
    node_num = 0
    while current is not None and node_num < list_length - rotate_amount - 1:
        current = current.next
        node_num += 1

    # set new head
    head = current.next

    # set current.next as the end of the list
    current.next = None

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = rotate_list(head, 3)
    print("Nodes of rotated LinkedList are: ", end="")
    result.print_list()


main()
