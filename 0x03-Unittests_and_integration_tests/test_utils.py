#!/usr/bin/env python3
""" test for utils module"""
import unittest
from unittest.mock import Mock, patch, MagicMock
from utils import access_nested_map
from utils import get_json
from utils import memoize
from parameterized import parameterized
from typing import Mapping, Any, Union, Callable


class TestAccessNestedMap(unittest.TestCase):
    """ Tests for access_nested_map fumc"""
    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, "a", {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Union[str, tuple], expected: Any):
        """ test function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, "a",),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_map_exception(self, nested_map: Mapping,
                                  path: Union[str, tuple]):
        """ tests for exceptions in access_nested_map func"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Tests to get_json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests.get')
    def test_get_json(self, url: str, test_payload: dict, mock_get):
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        result = get_json(url)
        mock_get.assert_called_once_with(url)
        self.assertEqual(result, test_payload)


class TestClass:
    """ A class to test memoize """
    def a_method(self):
        """ returns 42"""
        return 42

    @memoize
    def a_property(self):
        """ returns a method"""
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """ Test suite for memoize function """
    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method: MagicMock):
        """ tests memoize function"""
        obj = TestClass()

        first_call = obj.a_property
        second_call = obj.a_property

        self.assertEqual(first_call, 42)
        self.assertEqual(second_call, 42)

        mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
