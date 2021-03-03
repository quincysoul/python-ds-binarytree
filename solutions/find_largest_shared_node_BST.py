import binarytree

"""
Problem: For 2 Binary Search Trees, find the largest value node,
that is present in both trees.

1. Do not access capabilities of binarytree other than these properties: value, left, right
2. You may use binarytree.build(list) on the input Lists to convert to the binarytree data structure

  ______9______                  __8___
 /             \                /      \
0__         ____12             3       _13
   \       /      \           / \     /
    6     10       14        2   5   11
   / \      \               /
  1   7      11            0

tree_1 = [9, 0, 12, None, 6, 10, 14, None, None, 1, 7, None, 11]
tree_2 = [9, 0, 13, None, 8, 10, 14, None, None, 7, None, None, 12]
expected = 11
"""


class Solution:
    def find_largest_shared_node(self, tree_1_values, tree_2_values):
        tree_1 = binarytree.build(tree_1_values)
        tree_2 = binarytree.build(tree_2_values)
        # If I were to in-order traverse.
        # [0,1,6,7,9,10,11,12,14]
        # [0,2,3,5,8,11,13]


tree_1_values = [9, 0, 12, None, 6, 10, 14, None, None, 1, 7, None, 11]
tree_2_values = [9, 0, 13, None, 8, 10, 14, None, None, 7, None, None, 12]
solution = Solution()
res = solution.find_largest_shared_node(tree_1, tree_2)
# print(res)
