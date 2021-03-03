import unittest
import binarytree
from ...solutions.reverse_level_order_traversal import Solution


class Test_Reverse_Level_Order(unittest.TestCase):
    def test_reverse_level_order(self):
        """
        Tree should return reverse level order list
        """
        """
              ______8_____
             /            \
            4__         ___14
           /   \       /
          3     6     9
         /     / \     \
        0     5   7     12
        """

        expected = [0, 5, 7, 12, 3, 6, 9, 4, 14, 8]
        root = binarytree.build([8, 4, 14, 3, 6, 9, None, 0, None, 5, 7, None, 12])
        solution = Solution()
        self.assertEqual(expected, solution.reverse_level_order(root))

    def test_reverse_level_order_with_none_vals(self):
        """
        Tree should return reverse level order list, with None for empty l/r nodes
        """
        """
              ______8_____
             /            \
            4__         ___14
           /   \       /
          3     6     9
         /     / \     \
        0     5   7     12
        """

        expected = [0, None, 5, 7, None, 12, 3, 6, 9, None, 4, 14, 8]
        root = binarytree.build([8, 4, 14, 3, 6, 9, None, 0, None, 5, 7, None, 12])
        solution = Solution()
        self.assertEqual(expected, solution.reverse_level_order(root, True))
