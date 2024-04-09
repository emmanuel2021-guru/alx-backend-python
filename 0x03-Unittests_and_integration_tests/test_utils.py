#!/usr/bin/env python3

"""
Module to demonstrate the use of the unittest module
"""

import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test Method
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

# if __name__ == "__main__":
#     unittest.main()