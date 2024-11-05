#!/usr/bin/env python3
""" Test module for Client module """
import unittest
from client import GithubOrgClient
from unittest.mock import Mock, patch, MagicMock, PropertyMock
from parameterized import (parameterized,
                           parameterized_class)
from utils import get_json
from typing import Dict, List, Any
from fixtures import (org_payload,
                      repos_payload,
                      expected_payload,
                      apache2_repos)


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

    @parameterized.expand([
                         ({"license": {"key": "my_license"}},
                             "my_license", True),
                         ({"license": {"key": "other_license"}},
                             "my_license", False)
                         ])
    def test_has_license(self, repo: Dict[str, Any],
                         license_key: str, expected: bool):
        """ tests has_license func """
        client = GithubOrgClient('Alx')
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)

@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload, "expected_repos": expected_repos, "apache2_repos": apache2_repos},
])

class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the class-level patcher for requests.get."""
        cls.get_patcher = patch("client.requests.get")
        cls.mock_get = cls.get_patcher.start()
        def get_json_side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return cls.org_payload
            elif url == "https://api.github.com/orgs/google/repos":
                return cls.repos_payload
            return None

        cls.mock_get.return_value.json.side_effect = get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher after tests are done."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method returns expected repository names."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_apache2_repos(self):
        """Test that the public_repos method filters for Apache 2.0 licensed repos."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)



if __name__ == "__main__":
    unittest.main()
