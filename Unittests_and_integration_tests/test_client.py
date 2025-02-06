#!/usr/bin/env python3
'''
Test client.py
'''
from client import GithubOrgClient
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
from typing import Any, Dict, List


class TestGithubOrgClient(unittest.TestCase):
    '''GithubOrgClient
    '''
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org_url, mock_get_json):
        '''Tests that GithubOrgClient returns expected value
        '''
        request = GithubOrgClient(org_url)
        request.org
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_url)
        )

    def test_public_repos_url(self):
        '''Test that _public_repos_url returns mocked payload
        '''
        expected = "https://test.com/test"
        payload: dict = {"repos_url": expected}
        mockme = 'client.GithubOrgClient.org'
        with patch(mockme, PropertyMock(return_value=payload)):
            qry = GithubOrgClient("test")
            rsp = qry._public_repos_url

            self.assertEqual(rsp, expected)

    @patch("client.get_json")
    def test_public_repos(self, get_json_mock):
        '''Test public_repos for expected output
        '''
        expected: str = "http://test.com/test"
        val1: str = "ASTR"
        val2: str = "GEOS"
        get_json_mock.return_value = ([
            {"name": val1},
            {"name": val2}
        ])
        with patch.object(
            GithubOrgClient, "_public_repos_url", mockme=PropertyMock
        ) as _public_repos_url_mock:
            _public_repos_url_mock.return_value = expected
            qry = GithubOrgClient("test")
            rsp = qry.public_repos()

            self.assertEqual(rsp, [val1, val2])
            get_json_mock.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license, expected):
        '''Test license checker
        '''
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration tests for GithubOrgClient
    '''
    org_payload: Dict[str, str]
    repos_payload: List[Dict[str, Any]]
    expected_repos: List[str]
    apache2_repos: List[str]

    @classmethod
    def setUpClass(cls):
        '''Setup
        '''
        def get_payload(url):
            '''Gets mocked url
            '''
            mock_response = Mock()
            org = GithubOrgClient.ORG_URL.format(org="test")

            if url == org:
                mock_response.json.return_value = cls.org_payload
            elif url == cls.org_payload.get("repos_url"):
                mock_response.json.return_value = cls.repos_payload
            else:
                mock_response.json.return_value = {}

            return mock_response

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        '''Teardown class after test
        '''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''Test that public_repos gets expected data
        '''
        qry = GithubOrgClient("test")
        self.assertEqual(qry.public_repos(), self.expected_repos)
