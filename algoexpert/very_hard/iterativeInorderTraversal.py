# O(n) time | O(n) space
def iterativeInOrderTraversal_stack(tree, callback):
    stack = []
    if tree is not None:
        curr = tree

    while stack or curr is not None:
        # push root values and then all left values
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        callback(curr)

        curr = curr.right


# O(n) time | O(1) space
def iterativeInOrderTraversal(tree, callback):
    prev = None
    curr = tree
    next = None

    while curr is not None:
        # if the previous node is our parent
        if prev is None or prev == curr.parent:
            # we either want to keep going left
            if curr.left is not None:
                next = curr.left
            # or call the callback function on the current node, and
            #     move to the next node in the right subtree
            else:
                callback(curr)
                next = curr.right if curr.right is not None else curr.parent
        # if the previous node is our left subtree we are returning
        #     up from that subtree, so callback on current node, and
        #     start exploring the right subtree
        elif prev == curr.left:
            callback(curr)
            next = curr.right if curr.right is not None else curr.parent
        # else, we are returning up from the right subtree, so return to
        #     our parent
        else:
            next = curr.parent
        prev = curr
        curr = next
    pass
