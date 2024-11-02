#!/usr/bin/env python3
""" test for utils module"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Mapping, Any, Union


class TestAccessNestedMap(unittest.TestCase):
    """ Tests for access_nested_map fumc"""
    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, "a", {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Union[str, tuple], expected: Any):
        """ test function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)



if __name__ == "__main__":
    unittest.main()
