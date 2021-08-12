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

# while version
def findClosestValueInBst_while(tree, target):
    # Write your code here.
	closest = tree.value
	while tree:
		# update the closest value if neces
		if abs(target - tree.value) < abs(target - closest):
			closest = tree.value
		if target > tree.value:
			tree = tree.right
		elif target < tree.value:
			tree = tree.left
		else:
			return closest
	return closest

# Jua version
def findClosestValueInBst(tree, target):
    # Write your code here.
    cur = tree
    closest = [cur, abs(cur.value - target)]
    while cur.left != None or cur.right != None:
        if cur.value == target:
            return target
        elif cur.value > target and cur.left:
            cur = cur.left
        elif cur.value < target and cur.right:
            cur = cur.right
        else: 
            break
            
        if closest[1] > abs(cur.value - target):
            closest = [cur, abs(cur.value - target)]
		
    return closest[0].value

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

one = BST(1); five = BST(5); fourteen = BST(14); twentytwo = BST(22)
two = BST(2); two.left = one
five_ = BST(5); five_.left = two; five_.right = five
thirteen = BST(13); thirteen.right = fourteen
fifteen = BST(15); fifteen.left = thirteen; fifteen.right = twentytwo
ten = BST(10); ten.left = five_; ten.right = fifteen

# for i in range(5555555):
#     find_closest_value_in_bst(ten, 12)
# print(find_closest_value_in_bst(ten, 12))
# for i in range(5555555):
#     findClosestValueInBst_while(ten, 12)
# print(findClosestValueInBst_while(ten, 12))
# for i in range(5555555):
#     findClosestValueInBst(ten, 12)
# print(findClosestValueInBst(ten, 12))


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

ten = BST(10)
five = BST(5); fifteen = BST(15)
ten.left = five; ten.right = fifteen
two = BST(2); five_ = BST(5); thirteen = BST(13); twentytwo = BST(22)
five.left = two; five.right = five_; fifteen.left = thirteen; fifteen.right = twentytwo
one = BST(1); fourteen = BST(14)
two.left = one; thirteen.right = fourteen

# for i in range(5555555):
#     findClosestValueInBst_while(ten, 12)
# print(findClosestValueInBst_while(ten, 12))

def return_closest_node_value(tree, target, closest):
    # base case
    if not tree:
        return closest

    # update closest value if necessary
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target > tree.value:
        return return_closest_node_value(tree.right, target, closest)
    elif target < tree.value:
        return return_closest_node_value(tree.left, target, closest)
    else:
        return closest


def findClosestValueInBst_recursion(tree, target):
    return return_closest_node_value(tree, target, tree.value)

for i in range(5555555):
    findClosestValueInBst_recursion(ten, 12)
print(findClosestValueInBst_recursion(ten, 12))
