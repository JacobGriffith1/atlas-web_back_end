#!/usr/bin/env python3
'''
Test client.py
'''
from client import GithubOrgClient
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized


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
