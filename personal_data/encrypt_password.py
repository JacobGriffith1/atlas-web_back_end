#!/usr/bin/env python3
'''
MODULE FOR PASSWORD ENCRYPTION AND VALIDATION
'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    Function hashes password
    '''
    encoded_pw = password.encode()
    hashed_pw = bcrypt.hashpw(encoded_pw, bcrypt.gensalt())

    return hashed_pw


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    Function checks if pw matches hashed pw
    '''
    validator = False
    encoded_pw = password.encode()
    if bcrypt.checkpw(encoded_pw, hashed_password):
        validator = True
    return validator
