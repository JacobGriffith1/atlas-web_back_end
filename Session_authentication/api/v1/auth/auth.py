#!/usr/bin/env python3
'''
MODULE FOR API AUTHENTICATION
'''
from flask import request
from typing import List, TypeVar
import os


class Auth():
    '''
    Authentication class
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        Checks if authentication is required
        '''
        if path is None or excluded_paths is None or excluded_paths == '':
            return True
        elif path[len(path) - 1] != '/':
            path += '/'
        for item in excluded_paths:
            astr = item.find("*")
            if astr != -1 and len(path) >= len(item):
                cpyPath = path[: astr]
                if cpyPath == item[: astr]:
                    return False
            elif path == item:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        '''
        Returns auth header
        '''
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Returns current user info
        '''
        return None

    def session_cookie(self, request=None):
        '''
        session_cookie
        '''
        if request is None:
            return None
        name_var = os.getenv('SESSION_NAME')
        return request.cookies.get(name_var)
