#!/usr/bin/env python3
'''
MODULE FOR PASSWORD ENCRYPTION
'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    Function hashes password
    '''
    encoded_pw = password.encode()
    hashed_pw = bcrypt.hashpw(encoded_pw, bcrypt.gensalt())

    return hashed_pw
