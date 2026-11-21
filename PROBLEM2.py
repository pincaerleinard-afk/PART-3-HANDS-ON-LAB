# Problem 2: Height & Size Toolkit

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def size(node):
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)


def height(node):
    # Height is measured in edges. An empty tree is -1
    # and a tree containing only the root has height 0.
    if node is None:
        return -1

    left_height = height(node.left)
    right_height = height(node.right)
    return 1 + max(left_height, right_height)


def iterative_size(root):
    if root is None:
        return 0

    queue = [root]
    count = 0

    while queue:
        current = queue.pop(0)
        count += 1

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return count


if __name__ == "__main__":
    # Build the same nine-node tree from Problem 1.
    root = Node(15)
    root.left = Node(10)
    root.right = Node(25)

    root.left.left = Node(4)
    root.left.right = Node(12)
    root.right.left = Node(20)
    root.right.right = Node(30)

    root.left.left.left = Node(2)
    root.left.left.right = Node(6)

    print("size =", size(root))
    print("height =", height(root))
    print("iterative_size =", iterative_size(root))
