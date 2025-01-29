#!/bin/usr/env python3
'''
AUTHENTICATION MODULE
'''
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    '''
    BasicAuth class
    '''

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''
        E.B.A.H. function
        '''
        if (authorization_header is None
            or type(authorization_header) is not str
            or authorization_header[0:6] != 'Basic '):
            return None
        return authorization_header[6:]
    
    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        '''
        D.B.A.H. function
        '''
        if (base64_authorization_header is None
            or type(base64_authorization_header) is not str):
            return None
        try:
            b64_bytes = base64_authorization_header.encode("utf-8")
            str_bytes = base64.b64decode(b64_bytes)
            str_demo = str_bytes.decode("utf-8")
            return str_demo
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        '''
        E.U.C. function
        '''
        if (decoded_base64_authorization_header is None
            or type(decoded_base64_authorization_header) is not str
            or decoded_base64_authorization_header.find(":") == -1):
            return None, None
        separator = decoded_base64_authorization_header.find(":")
        user = decoded_base64_authorization_header[:separator]
        pw = decoded_base64_authorization_header[separator + 1:]
        return user, pw

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str
                                     ) -> TypeVar('User'):
        '''
        U.O.F.C. function
        '''
        if (user_email is None
            or type(user_email) is not str
            or user_pwd is None
            or type(user_pwd) is not str):
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None
        if len(user) == 0:
            return None
        valid_pw = user[0].is_valid_password(user_pwd)
        if not valid_pw:
            return None
        return user[0]

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        current_user function
        '''
        header = self.authorization_header(request)
        auth = self.extract_base64_authorization_header(header)
        decode = self.decode_base64_authorization_header(auth)
        cred = self.extract_user_credentials(decode)
        return self.user_object_from_credentials(cred[0], cred[1])
