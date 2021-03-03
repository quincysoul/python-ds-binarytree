import unittest
from ...solutions.validity_of_BST_eop14_1 import Solution


class Test_BST_Validity(unittest.TestCase):
    def test_valid_tree_returns_true(self):
        """
        A valid tree should return true.
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

        expected = True
        input = [8, 4, 14, 3, 6, 9, None, 0, None, 5, 7, None, 12]
        solution = Solution()
        self.assertEqual(expected, solution.is_valid_tree(input))

    def test_valid_tree_returns_false(self):
        """
        A NOT valid tree should return False.
        """
        """
              ______8_____
             /            \
            4__         ___14
           /   \       /
          3     6     9
         /     / \     \
        0     3   7     12
        """

        expected = False
        input = [8, 4, 14, 3, 6, 9, None, 0, None, 3, 7, None, 12]
        solution = Solution()
        self.assertEqual(expected, solution.is_valid_tree(input))
