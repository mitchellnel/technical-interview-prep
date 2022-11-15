# O(n) time | O(n) space
def inOrderTraverse(tree, array):
    # inorder is left,self,right
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


# O(n) time | O(n) space
def preOrderTraverse(tree, array):
    # preorder is self,left,right
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


# O(n) time | O(n) space
def postOrderTraverse(tree, array):
    # postorder is left,right,self
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array


# O(n) time | O(n) space
def inOrderTraverse_iterative(tree, array):
    # inorder is left,self,right
    stack = []

    if tree is not None:
        curr = tree

    while len(stack) > 0 or curr is not None:
        # push root value and then all left values
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        array.append(curr.value)

        curr = curr.right

    return array


# O(n) time | O(n) space
def preOrderTraverse_iterative(tree, array):
    # preorder is self,left,right
    stack = []

    if tree is not None:
        stack.append(tree)

    while len(stack) > 0:
        curr = stack.pop()
        # append root value
        array.append(curr.value)

        # push right so we look at it last
        if curr.right is not None:
            stack.append(curr.right)

        # then push left so we look at it first
        if curr.left is not None:
            stack.append(curr.left)

    return array


# O(n) time | O(n) space
def postOrderTraverse_iterative(tree, array):
    # postorder is right,left,self
    stack = []

    if tree is not None:
        stack.append(tree)

    while len(stack) > 0:
        print(stack)
        curr = stack.pop()
        # append root value
        array.append(curr.value)

        # push left so we look at it last
        if curr.left is not None:
            stack.append(curr.left)

        # then push right so we look at it first
        if curr.right is not None:
            stack.append(curr.right)

    # our array is currently self,left,right
    # so reverse it to get right,left,self
    array.reverse()

    return array
