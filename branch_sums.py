# Branch Sums
# Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.

# A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node.

# Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

# Sample Input
# tree =     1
#         /     \
#        2       3
#      /   \    /  \
#     4     5  6    7
#   /   \  /
#  8    9 10
# Sample Output
# [15, 16, 18, 10, 11]
# // 15 == 1 + 2 + 4 + 8
# // 16 == 1 + 2 + 4 + 9
# // 18 == 1 + 2 + 5 + 10
# // 10 == 1 + 3 + 6
# // 11 == 1 + 3 + 7

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = BST(1)
root.left = BST(2)
root.left.left = BST(4)
root.left.left.left = BST(8)
root.left.left.right = BST(9)
root.left.right = BST(5)
root.left.right.left = BST(10)
root.right = BST(3)
root.right.left = BST(6)
root.right.right = BST(7)

def branch_sums(root):
    results = []
    current_sum = 0
    branch_sum(root, current_sum, results)
    return results

def branch_sum(node, current_sum, results):
    if not node:
        return
    current_sum += node.value
    if not node.left and not node.right:
        results.append(current_sum)
    if node.left:
        branch_sum(node.left, current_sum, results)
    if node.right:
        branch_sum(node.right, current_sum, results)

# Sample Input
# tree =   10
#        /     \
#       5      15
#     /   \   /   \
#    2     5 13   22
#  /           \
# 1            14
ten = BST(10)
five = BST(5); fifteen = BST(15)
ten.left = five; ten.right = fifteen
two = BST(2); five_ = BST(5); thirteen = BST(13); twentytwo = BST(22)
five.left = two; five.right = five_; fifteen.left = thirteen; fifteen.right = twentytwo
one = BST(1); fourteen = BST(14)
two.left = one; thirteen.right = fourteen

# print(branch_sums(ten)) # [18,20,52,47]
# for i in range(555555):
#     branch_sums(root)
# print(branch_sums(root)) # [15, 16, 18, 10, 11]

# Jua version
def branch_sums1(root):
    nodestack = []
    if root.right:
        nodestack.append(root.right)
    if root.left:
        nodestack.append(root.left)
    if not root.right and not root.left:
        return [root.value] 

    cum_sums = {root: root.value}
    parent_nodes = {root.right: root, root.left: root}
    sums = []
    while nodestack:
        cur_node = nodestack.pop()
        cum_sums[cur_node] = cum_sums[parent_nodes[cur_node]] + cur_node.value 
        if cur_node.right:
            parent_nodes[cur_node.right] = cur_node
            nodestack.append(cur_node.right)
        if cur_node.left:
            parent_nodes[cur_node.left] = cur_node
            nodestack.append(cur_node.left)
        if not cur_node.left and not cur_node.right:
            sums.append(cum_sums[cur_node])
    return sums

# print(branch_sums1(ten)) # [18,20,52,47]
# for i in range(555555):
#     branch_sums1(root)
# print(branch_sums1(root)) # [15, 16, 18, 10, 11]
