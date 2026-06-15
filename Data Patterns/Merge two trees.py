class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def mergeTrees(t1, t2):

    if t1 is None:
        return t2

    if t2 is None:
        return t1

    t1.data += t2.data

    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)

    return t1


def inorder(root):

    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Sample Trees

root1 = Node(1)
root1.left = Node(3)
root1.right = Node(2)

root2 = Node(2)
root2.left = Node(1)
root2.right = Node(3)

merged = mergeTrees(root1, root2)

print("Inorder of Merged Tree:")
inorder(merged)