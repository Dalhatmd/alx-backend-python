#!/usr/bin/python3
""" Test module for Client module """
import unittest
from client import GithubOrgClient
from unittest.mock import Mock, patch, MagicMock
from parameterized import parameterized
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """ GitHubOrgClient Test suite """
    @parameterized.expand([("google",), ("abc",)])
    @patch('utils.requests.get')
    def test_org(self, org_name, mock_get_json):
        """ tests for correct org return """
        mock_response = MagicMock()
        mock_response.json.return_value = {"login": "test_org",
                                           "id": 12345,
                                           "repos_url":
                                           "https://api.github.com\
                                                   /orgs/test_org/repos"}
        mock_get_json.return_value = mock_response
        client = GithubOrgClient(org_name)
        result = client.org
        expected_url = f"https://api.github.com/orgs/{org_name}"

        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, mock_response.json.return_value)


if __name__ == "__main__":
    unittest.main()
