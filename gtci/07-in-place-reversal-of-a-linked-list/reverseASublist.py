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

    curr = head
    prev = None

    i = 0

    # get to node p
    while curr is not None and i < p - 1:
        prev = curr
        curr = curr.next

        i += 1

    # after skipping p-1 nodes, curr now points to p

    # we are interested in three parts of the linked list:
    #   - the part before the pth node
    #   - the part between p and q
    #   - the part after the qth node

    # we need to connect the last node of the first part to the start of the
    #   reversed linked list
    last_node_before_sublist = prev

    # we need to connect the last node of the sublist to the start of the part
    #   after the qth node
    last_node_in_sublist = curr

    # reverse the nodes in between p and q
    i = 0
    while curr is not None and i < q - p + 1:
        temp = curr.next

        curr.next = prev
        prev = curr

        curr = temp

        i += 1

    # connect reversed sublist to the part of the linked list before the
    #   pth node
    if last_node_before_sublist is not None:
        # prev is currently the first node of the reversed sublist
        last_node_before_sublist.next = prev
    else:
        # this means that p == 1, i.e. we are changing the first node of the
        #   linked list
        head = prev

    # connect reversed sublist to last part
    last_node_in_sublist.next = curr

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
