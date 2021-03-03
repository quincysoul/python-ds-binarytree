import unittest
import binarytree
from ...solutions.k_largest_elements_BST_eop14_3 import Solution


class Test_BST_Greater_Than(unittest.TestCase):
    def test_finds_k_largest(self):
        """
        Should return [14,12,9,8,4], for k = 5.
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

        expected = [14, 12, 9, 8, 4]
        input = [8, 4, 14, 3, 6, 9, None, 0, None, 5, 7, None, 12]
        solution = Solution()
        actual = solution.k_largest_elements(binarytree.build(input), 5)
        self.assertEqual(expected, actual)

    def test_finds_k_largest_2(self):
        """
        Should return [11, 10, 7, 5, 4, 3], for k = 6.
        """
        """
              __5
             /   \
            3     7
           / \     \
          1   4     10
         /            \
        0              11
        """

        expected = [11, 10, 7, 5, 4, 3]
        input = [5, 3, 7, 1, 4, None, 10, 0, None, None, None, None, None, None, 11]
        solution = Solution()
        actual = solution.k_largest_elements(binarytree.build(input), 6)
        self.assertEqual(expected, actual)
