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


def reverse_every_k_element_sublist(head, k):
    if k <= 1 or head is None:
        return head

    current = head
    previous = None
    while True:
        node_before_sublist = previous
        last_node_in_sublist = current

        next = None
        node_num = 0

        # reverse until k
        while current is not None and node_num < k:
            # temp store the next node to look at
            next = current.next

            # reverse the current node
            current.next = previous
            previous = current

            # look at the next node
            current = next
            node_num += 1

        # connect the node before the sublist to the reversed sublist
        if node_before_sublist is not None:
            # the first node of the sublist is now previous
            node_before_sublist.next = previous
        else:
            head = previous

        # connect last node in the reversed sublist to the rest of the list
        last_node_in_sublist.next = current

        # only when we reach the end of the list do we break
        if current is None:
            break
        previous = last_node_in_sublist

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse_every_k_element_sublist(head, 3)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


main()
