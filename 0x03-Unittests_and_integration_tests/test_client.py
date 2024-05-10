#!/usr/bin/env python3
"""testing client file"""

from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import unittest
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """testing class"""

    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name: str, mock_get: Mock) -> None:
        """test func 1"""
        org_cl = GithubOrgClient(org_name)
        self.assertEqual(org_cl.org, {"payload": True})
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get.assert_called_once_with(url)

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org) -> None:
        """test func 2"""
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = payload
        github_org_client = GithubOrgClient("google")
        self.assertEqual(github_org_client._public_repos_url, payload["repos_url"])

    @patch("client.get_json", return_value=[{"name": "repo1"}, {"name": "repo2"}])
    def test_public_repos(self, mock_get_json) -> None:
        """test func 3"""
        with patch(
            "client.GithubOrgClient._public_repos_url", new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/google/repos"
            )
            github_org_client = GithubOrgClient("google")
            self.assertEqual(github_org_client.public_repos(), ["repo1", "repo2"])
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, assertion) -> None:
        """doc doc doc"""
        github_org_client = GithubOrgClient("google")
        self.assertEqual(github_org_client.has_license(repo, license_key), assertion)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"), TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """testing class 2"""

    @classmethod
    def setUpClass(cls):
        """doc doc doc"""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """test func 4"""

            class MockResponse:
                def __init__(self, json_data):
                    self.json_data = json_data

                def json(self):
                    return self.json_data

            if url.endswith("/orgs/google"):
                return MockResponse(cls.org_payload)
            elif url.endswith("/orgs/google/repos"):
                return MockResponse(cls.repos_payload)
            else:
                return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """test func 5"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test func 6"""
        github_org_client = GithubOrgClient("google")
        self.assertEqual(github_org_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """test func 7"""
        github_org_client = GithubOrgClient("google")
        self.assertEqual(
            github_org_client.public_repos(license="apache-2.0"), self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
