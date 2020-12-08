import binarytree
from collections import deque


class Solution:
    def binary_tree_print_center(self):
        tree_list = [9, 7, 0, 2, 10, 3, 13, 8, None, None, None, 5, None, 4, 11]

        """
        Problem: For a binary tree, print values in level-order
        But also, sort by closest to center (where L is closest and R second closest)
              ____9____
             /         \
            7           0__
           / \         /    \
          2  10       3     13
         /           /     /  \
        8           5     4    11

        Expected: 9,7,0,10,3,2,13,5,4,8,11

        Do not access capabilities of binarytree other than these properties:
        Node
        ---
        value
        left
        right
        """
        root = binarytree.build(tree_list)
        # Pre sorted
        pre_sorted = []
        que = deque()
        # Level order traversal
        level = 0
        distance = 0
        que.append((root, level, distance, None))
        element = que.popleft()

        print(f"START: {root.value}")

        while element:
            pre_sorted.append(element)
            node = element[0]
            level = element[1]
            distance = element[2]
            prev = element[3]
            print(f"Traversing node: {node.value,level,distance,prev}")

            if node.left:
                if prev == "right":
                    que.append((node.left, level + 1, distance - 1, "left"))
                else:
                    que.append((node.left, level + 1, distance + 1, "left"))
            if node.right:
                if prev == "left":
                    que.append((node.right, level + 1, distance - 1, "right"))
                else:
                    que.append((node.right, level + 1, distance + 1, "right"))

            if que:
                element = que.popleft()
            else:
                element = None

            # node = None
        expected = [9, 7, 0, 10, 3, 2, 13, 5, 4, 8, 11]
        print("Expected:", expected)

        sorted_list = sorted(pre_sorted, key=self.sort_by_level_then_distance)
        # print("FULL LIST: ", sorted_list)
        res = []
        for tup in sorted_list:
            res.append(tup[0].value)
        print("Actual:  ", res)

    def sort_by_level_then_distance(self, tup):
        return (tup[1], tup[2])


solution = Solution()
res = solution.binary_tree_print_center()
# print(res)
