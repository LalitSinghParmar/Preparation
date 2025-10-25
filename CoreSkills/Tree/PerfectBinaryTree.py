class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class PerfectBinaryTree:
    '''
    A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level.
    All the internal nodes have a degree of 2.
    '''

    def calculateDepth(self, node:Node) -> int:
        if node is None:
            return 0
        return max(self.calculateDepth(node.left), self.calculateDepth(node.right)) + 1

    def isPerfectBinaryTree(self, node:Node, depth:int, level:int=0) -> bool:
        '''
        Recursively, a perfect binary tree can be defined as:
        1. If a single node has no children, it is a perfect binary tree of height h = 0,
        2. If a node has h > 0, it is a perfect binary tree if both of its subtrees are of height h - 1 and are non-overlapping.
        '''
        # Condition for empty tree
        if node is None:
            return True
        
        # Condition for leaf node, it's level should be equal to depth of tree to be perfect Binary tree
        if node.left is None and node.right is None:
            return depth == level + 1
        
        # Condition for if node doesn't have left or right subtree
        if (node.left is None and node.right is not None) or (node.right is None and node.left is not None):
            return False
        
        # Condition to check if left and right subtree is perfect binary tree or not
        return self.isPerfectBinaryTree(node.left, depth, level+1) and self.isPerfectBinaryTree(node.right, depth, level+1)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

bt = PerfectBinaryTree()
if bt.isPerfectBinaryTree(root, bt.calculateDepth(root)):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)

if bt.isPerfectBinaryTree(root, bt.calculateDepth(root)):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")
        