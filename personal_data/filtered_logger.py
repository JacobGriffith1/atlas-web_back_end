#!/usr/bin/env python3
'''
MODULE FOR FILTERING AND LOGGING INFORMATION
'''
import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''
    Function returns a log message obfuscated
    '''

    for field in fields:
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator,
                         message)
        return message
