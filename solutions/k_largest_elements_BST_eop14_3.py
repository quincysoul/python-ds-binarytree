import binarytree
from collections import deque, namedtuple

"""
Problem: For 1 Binary Search Tree, return the k largest elements
For simplifying tests, accept params as follows:
tree_root: binarytree.Node
k: int

Return: val of k largest elements in array.

      __5
     /   \
    3     7
   / \     \
  1   4     10
 /            \
0              11

-------------

-------------
Time Complexity:
O(N)
Space Complexity:
O(N)

-------------
"""


class Solution:
    def __init__(self):
        self.first_occurrence = None

    def k_largest_elements(self, tree_root, k):
        print(tree_root)

    def reverse_in_order(self, tree_root, k):
        root = tree_root

        tourist = root
        guide = root

        # while(tourist is not None):

        #     while(guide is not None):


# print(res)
