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
