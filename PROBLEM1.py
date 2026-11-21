# Problem 1: Tree Traversals

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)


def preorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")


def level_order(root):
    if root is None:
        return

    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


if __name__ == "__main__":
    # Build the tree shown in the activity.
    root = Node(15)
    root.left = Node(10)
    root.right = Node(25)

    root.left.left = Node(4)
    root.left.right = Node(12)
    root.right.left = Node(20)
    root.right.right = Node(30)

    root.left.left.left = Node(2)
    root.left.left.right = Node(6)

    print("Inorder:", end=" ")
    inorder(root)
    print()

    print("Preorder:", end=" ")
    preorder(root)
    print()

    print("Postorder:", end=" ")
    postorder(root)
    print()

    print("Level-order:", end=" ")
    level_order(root)
    print()
