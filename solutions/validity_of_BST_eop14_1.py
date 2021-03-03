import binarytree
from collections import deque, namedtuple

"""
Problem: For 1 Binary Search Tree, return if the binary search tree is valid.

      ______8_____
     /            \
    4__         ___14
   /   \       /
  3     6     9
 /     / \     \
0     5   7     12

-------------
Solution as shown: BFS.
-------------
Time Complexity:
O(N)
Space Complexity:
O(N)

-------------
Another possible solution is to do DFS or recursive in-order. 
You could compare ranges as here, but also you could write to an array and then
do 1 O(N) iteration and compare i-1 <= i <= i+1 in array and see if all True..
"""


class Solution:
    def __init__(self):
        self.que = deque()

    def is_valid_tree(self, tree_values):
        root = binarytree.build(tree_values)
        # print(root)
        Entry = namedtuple("Entry", ("node", "L", "R"))
        self.que.append(Entry(root, float("-inf"), float("inf")))

        while self.que:
            # print("continue que")
            front = self.que.popleft()

            if front.node is not None:
                if not front.L <= front.node.val <= front.R:
                    return False
                self.que.append(Entry(front.node.left, front.L, front.node.val))
                self.que.append(Entry(front.node.right, front.node.val, front.R))

        return True


# print(res)
