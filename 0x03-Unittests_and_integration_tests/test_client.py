#!/usr/bin/env python3
""" Test module for Client module """
import unittest
from client import GithubOrgClient
from unittest.mock import Mock, patch, MagicMock, PropertyMock
from parameterized import parameterized
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """ GitHubOrgClient Test suite """
    @parameterized.expand([("google",), ("abc",)])
    @patch('utils.requests.get')
    def test_org(self, org_name: str, mock_get_json: MagicMock):
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

    @parameterized.expand([("google",), ("abc",)])
    @patch.object(GithubOrgClient,
                  "_public_repos_url",
                  new_callable=PropertyMock)
    def test_public_repos_url(self, org_name, mock_public_repos_url):
        mock_public_repos_url.return_value = "https://api.github.com/orgs\
                /test_org/repos"
        client = GithubOrgClient(org_name)
        repos_url = client._public_repos_url
        self.assertEqual(repos_url, mock_public_repos_url.return_value)


if __name__ == "__main__":
    unittest.main()
