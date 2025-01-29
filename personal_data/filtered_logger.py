#!/usr/bin/env python3
'''
MODULE FOR FILTERING AND LOGGING INFORMATION
'''
import re
from typing import List
import logging
import mysql.connector
from os import getenv


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''
        Constructor method
        '''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''
        Filters values using filter_datum
        '''
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    '''
    Logging function
    '''
    log = logging.getLogger('user_data')
    log.setLevel(logging.INFO)
    log.propagate = False

    sh = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    sh.setFormatter(formatter)
    log.addHandler(sh)

    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''
    Function prevents dabase credentials from being added to code
    '''

    connectedDB = mysql.connector.connection.MySQLConnection(
        user=getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        dbName=getenv('PERSONAL_DATA_DB_NAME'))

    return connectedDB


def main():
    '''
    Retrieves a table and displays it filtered
    '''
    db = get_db()
    dbCursor = db.cursor()
    dbCursor.execute("SELECT * FROM users;")
    fields = [n[0] for n in dbCursor.description]

    log = get_logger()

    for row in dbCursor:
        rowString = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, fields))
        log.info(rowString.strip())

    dbCursor.close()
    db.close()


if __name__ == '__main__':
    main()
