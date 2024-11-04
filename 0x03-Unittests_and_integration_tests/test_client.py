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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Test the public_repos method of GithubOrgClient."""
        test_payload = {
            'repos_url': "https://api.github.com/users/microsoft/repos",
            'repos': [
                {
                    "id": 1234567,
                    "name": "vscode",
                    "private": False,
                    "owner": {
                        "login": "microsoft",
                        "id": 123456,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/microsoft/vscode",
                    "created_at": "2015-04-29T16:25:30Z",
                    "updated_at": "2024-11-01T12:00:00Z",
                    "has_issues": True,
                    "forks": 500,
                    "default_branch": "main",
                },
                {
                    "id": 2345678,
                    "name": "TypeScript",
                    "private": False,
                    "owner": {
                        "login": "microsoft",
                        "id": 123456,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/microsoft/TypeScript",
                    "created_at": "2012-10-01T22:00:00Z",
                    "updated_at": "2024-11-01T12:00:00Z",
                    "has_issues": True,
                    "forks": 200,
                    "default_branch": "main",
                },
                {
                    "id": 3456789,
                    "name": "PowerToys",
                    "private": False,
                    "owner": {
                        "login": "microsoft",
                        "id": 123456,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/microsoft/PowerToys",
                    "created_at": "2019-05-15T16:00:00Z",
                    "updated_at": "2024-11-01T12:00:00Z",
                    "has_issues": True,
                    "forks": 150,
                    "default_branch": "main",
                },
            ]
        }

        mock_get_json.return_value = test_payload["repos"]

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]

            client = GithubOrgClient("microsoft")

            self.assertEqual(
                client.public_repos(),
                [
                    "vscode",
                    "TypeScript",
                    "PowerToys",
                ],
            )

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
