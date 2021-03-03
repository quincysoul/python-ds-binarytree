import binarytree
from collections import deque, namedtuple

"""
Problem: For 1 Tree, print levels in reverse order.

      __5
     /   \
    3     7
   / \     \
  1   4     10
 /            \
0              11

Return: [0,11,1,4,10,3,7,5]

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

    def reverse_level_order(self, tree_root, contains_None=False):
        print("Determining reverse level order")
        res = []

        que = deque()
        que.append(tree_root)

        while que:
            node = que.popleft()
            if node is None:
                res.append(None)
                continue
            if node.right is not None:
                que.append(node.right)
            if contains_None == True and node.right is None and node.left is not None:
                que.append(None)

            if node.left is not None:
                que.append(node.left)
            if contains_None == True and node.left is None and node.right is not None:
                que.append(None)

            res.append(node.val)

        res.reverse()
        return res
