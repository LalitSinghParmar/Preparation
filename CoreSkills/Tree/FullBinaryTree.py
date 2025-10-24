class Node:
    def __init__(self, data:int) -> None:
        self.data = data
        self.left = None
        self.right = None


class FullBinaryTree:
    '''
    Full binary tree, also known as proper binary tree, is a special type of binary tree in which each parent/internal node has either 2 or 0 child node
    i : No. of internal nodes
    n : Total no. of nodes
    l : No. of leaf nodes
    h : No. of levels or height of tree

    l = i+1 = (2**h)-1 = (n+1)/2
    '''

    def isFullTree(self, node:Node) -> None:
        '''
        Checking if a tree is a full Tree or not. We'll consider a empty tree as full Binary tree
        '''

        # Empty tree condition
        if node is None:
            return True
        
        # leaf node condition
        if node.left is None and node.right is None:
            return True
        
        # internal node condition
        if node.left is not None and node.right is not None:
            # checking left sub tree and right sub tree
            return self.isFullTree(node.left) and self.isFullTree(node.right)
        
        return False
    

root = Node(1)
root.right = Node(3)
root.left = Node(2)

root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

bt = FullBinaryTree()
if bt.isFullTree(root):
    print("Binary tree is full binary tree")
else:
    print("Binary tree is not full binary tree")
