

class Node:
    # Initializing a tree node
    def __init__(self, data:int) -> None:
        self.data = data
        self.left = None
        self.right = None

class TreeTraversal:

    def preOrder(self, node:Node) -> None:
        '''
        pre-order traversal : root->left->right
        '''
        if node:
            print(node.data, end="->")
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node:Node) -> None:
        '''
        in-order traversal: left->root->right
        '''
        if node:
            self.inOrder(node.left)
            print(node.data, end="->")
            self.inOrder(node.right)

    def postOrder(self, node:Node) -> None:
        '''
        post-order traversal: left->right->root
        '''
        if node:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data, end="->")



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

traversal = TreeTraversal()
print("PreOrder traversal:")
traversal.preOrder(root)
print()
print("InOrder traversal:")
traversal.inOrder(root)
print()
print("PostOrder traversal:")
traversal.postOrder(root)
print()


