def find_closest_value_in_bst(tree, target):
    diffs = {}
    tmp_nodes = [tree]
    nodes_to_check = []
    while tmp_nodes:
        # if children, collect children to tmp_nodes 
        # and add current node to nodes_to_check
        current_node = tmp_nodes.pop()
        if current_node.left:
            tmp_nodes.append(current_node.left)
        if current_node.right:
            tmp_nodes.append(current_node.right)
        nodes_to_check.append(current_node)
    # check nodes in array by pop
    for node in nodes_to_check:
        diff = abs(node.value - target)
        diffs[node.value] = diff
    return min(diffs, key = diffs.get)
    # closest = {}
    # for i, diff in enumerate(diffs):
    #     if i == 0:
    #         closest = {diff: diffs[diff]}
    #     else:
    #         if diffs[diff] < list(closest.values())[0]:
    #             closest = {diff: diffs[diff]}
    # return list(closest.keys())[0]

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

one = BST(1)
five = BST(5)
fourteen = BST(14)
twentytwo = BST(22)
two = BST(2)
two.left = one
five_ = BST(5)
five_.left = two
five_.right = five
thirteen = BST(13)
thirteen.right = fourteen
fifteen = BST(15)
fifteen.left = thirteen
fifteen.right = twentytwo
ten = BST(10)
ten.left = five_
ten.right = fifteen

print(find_closest_value_in_bst(ten, 12))


# Find Closest Value In BST
# Write a function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest value to that target value contained in the BST.

# You can assume that there will only be one closest value.

# Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

# Sample Input
# tree =   10
#        /     \
#       5      15
#     /   \   /   \
#    2     5 13   22
#  /           \
# 1            14
# target = 12
# Sample Output
# 13