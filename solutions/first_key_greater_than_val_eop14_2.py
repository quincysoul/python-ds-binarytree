import binarytree
from collections import deque, namedtuple

"""
Problem: For 1 Binary Search Tree, return the next higher number, to the
input value.

      ______8_____
     /            \
    4__         ___14
   /   \       /
  3     6     9
 /     / \     \
0     5   7     12

:: Notes:
Sometimes this could be phrased as, find the first key greater than a given value.
-------------
Solution as shown: BFS.
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

    def first_key_greater_equal_than_value(self, tree_values, value):
        root = binarytree.build(tree_values)
        # print(root)
        res = None
        self.first_occurrence = root

        if value >= root.right.val:
            self.search(root.right, value)
        else:
            self.search(root.left, value)

        return self.first_occurrence

    def search(self, node, value):

        if node:
            # print(f"Traversing search for value> {value}, node is: {node.val}")

            if value > node.val:
                self.search(node.right, value)
            elif value < node.val:
                self.first_occurrence = node
                self.search(node.left, value)


# print(res)
