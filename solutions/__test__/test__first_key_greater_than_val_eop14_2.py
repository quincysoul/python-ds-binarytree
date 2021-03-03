import unittest
import binarytree
from ...solutions.first_key_greater_than_val_eop14_2 import Solution


class Test_BST_Greater_Than(unittest.TestCase):
    def test_finds_next_highest_value(self):
        """
        Should find value 6 if input value is 5.
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

        expected = "\n  6\n / \\\n5   7\n"
        input = [8, 4, 14, 3, 6, 9, None, 0, None, 5, 7, None, 12]
        solution = Solution()
        actual = solution.first_key_greater_equal_than_value(input, 5)
        self.assertEqual(
            str(expected), str(solution.first_key_greater_equal_than_value(input, 5))
        )

    def test_finds_next_highest_value_2(self):
        """
        Should find value 8 if input value is 7.
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

        input = [8, 4, 14, 3, 6, 9, None, 0, None, 5, 7, None, 12]
        tree = binarytree.build(input)
        expected = str(tree)
        solution = Solution()
        self.assertEqual(
            expected, str(solution.first_key_greater_equal_than_value(input, 7))
        )

    def test_finds_next_highest_value_if_input_val_doesnt_exist(self):
        """
        Should find value 8 if input value is not existent (100)
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

        input = [8, 4, 14, 3, 6, 9, None, 0, None, 5, 7, None, 12]
        tree = binarytree.build(input)
        expected = str(tree)
        solution = Solution()
        self.assertEqual(
            expected, str(solution.first_key_greater_equal_than_value(input, 100))
        )

