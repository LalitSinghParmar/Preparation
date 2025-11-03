###################################################
# Balance BT is a tree which follows below conditions:
# 1. difference between the left and the right subtree for any node is not more than one
# 2. the left subtree is balanced
# 3. the right subtree is balanced
#
# eg: Below is the example of balanced BT-
#           1
#          / \
#         2   3
#        / \
#       4   5
# 
# Below is not a balanced BT-
#            1
#           / \
#          2   3
#         / \
#        4   5
#            /
#           6
#
###############################################



class Node:

    def __init__(self, data:int) -> None:
        self.data = data
        self.left = None
        self.right = None


class Height:
    def __init__(self) -> None:
        self.height = 0

def is_balanced_BT(node:Node, height:Height) -> bool:
    left_height = Height()
    right_height = Height()
    if node is None:
        return True
    
    left_subtree = is_balanced_BT(node.left, left_height)
    right_subtree = is_balanced_BT(node.right, right_height)

    height.height = 1 + max(left_height.height, right_height.height)
    if abs(left_height.height - right_height.height) <= 1:
        return left_subtree and right_subtree
    
    return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

if is_balanced_BT(root,Height()):
    print("Tree is a balance binary tree")

else:
    print("Tree is not a balance binary tree")