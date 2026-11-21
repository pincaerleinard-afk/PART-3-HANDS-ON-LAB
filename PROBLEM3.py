# Problem 3: Binary Search Tree (BST) from Scratch

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key. Duplicate keys are ignored."""
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root

        while True:
            if key == current.key:
                return  # Ignore duplicates

            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right

    def search(self, key):
        """Return True if key exists; otherwise return False."""
        current = self.root

        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return False

    def delete(self, key):
        """Delete a key if it exists."""
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete_node(node.left, key)
        elif key > node.key:
            node.right = self._delete_node(node.right, key)
        else:
            # Case 1: No child
            if node.left is None and node.right is None:
                return None

            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: Two children
            # Replace this node with the smallest key in its right subtree.
            successor = self._minimum(node.right)
            node.key = successor.key
            node.right = self._delete_node(node.right, successor.key)

        return node

    def _minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder(self):
        """Return all keys in ascending order as a list."""
        result = []

        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            result.append(node.key)
            traverse(node.right)

        traverse(self.root)
        return result


if __name__ == "__main__":
    bst = BST()

    for key in [50, 30, 70, 20, 40, 60, 80, 35, 45]:
        bst.insert(key)

    print(bst.inorder())  # line A
    print(bst.search(35))  # line B
    print(bst.search(99))  # line C

    bst.delete(20)  # delete a leaf
    bst.delete(40)  # delete a node with two children
    print(bst.inorder())  # line D
