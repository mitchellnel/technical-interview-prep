# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList):
    if linkedList is None:
        return None

    cur_node = linkedList

    while cur_node is not None:
        if cur_node.next is None:
            return linkedList
        elif cur_node.value == cur_node.next.value:
            cur_node.next = cur_node.next.next
        else:
            cur_node = cur_node.next

    return linkedList
