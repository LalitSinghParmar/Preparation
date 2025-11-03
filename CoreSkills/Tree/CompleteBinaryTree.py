###########################################################
# A Complete Binary Tree is a binary tree in which:
# 
# 1. All levels are completely filled, except possibly the last level, and
# 2. All nodes in the last level are as far left as possible.
#
# eg. Complete Binary Tree
#        1
#      /   \
#     2     3
#    / \   /
#   4   5 6
# This is a complete binary tree because:
# 1.Every level except the last is full.
# 2.The last level (4, 5, 6) is filled from left to right.
# ---------------------------------------------
#  Not a Complete Binary tree
#        1
#      /   \
#     2     3
#      \   /
#       5 6
#  Here, node 2 has a right child but no left child, which violates the left-to-right filling rule.
#
###########################################################

class Node:
    def __init__(self, data:int) -> None:
        self.data = data
        self.left = None
        self.right = None
        
def count_node(node:Node) -> int:
    if node is None:
        return 0
    return 1 + count_node(node.left) + count_node(node.right)

def is_complete_BT(node:Node, index:int, node_cnt:int) -> bool:
    if node is None:
        return True
    
    if index >= node_cnt:
        return False
    
    return is_complete_BT(node.left, 2*index+1, node_cnt) and is_complete_BT(node.right, 2*index+2, node_cnt)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

if is_complete_BT(root, 0, count_node(root)):
    print("Tree is a complete Binary Tree")

else:
    print("Tree is not a complete Binary Tree")