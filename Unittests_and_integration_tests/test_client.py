#!/usr/bin/env python3
'''
Test client.py
'''
from client import GithubOrgClient
import unittest
from unittest.mock import patch
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
