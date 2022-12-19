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


def reverse_sublist(head, p, q):
    if p == q:
        return head

    current = head
    previous = None

    node_num = 0

    # get to node p
    while current is not None and node_num < p:
        previous = current
        current = current.next

        node_num += 1

    # previous is now node p - 1
    # it will be the node before the sublist, we need to store it to connect it to the reversed
    #   sublist
    node_before_sublist = previous

    # current is now node p
    # it will be the last node in the sublist, we need to store it to connect the reversed sublist
    #   to the rest of the list
    last_node_in_sublist = current

    # reverse until q
    while current is not None and node_num < q + 1:
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

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse_sublist(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


main()
