#!/usr/bin/python
import time

class CustomException(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

def validate_pseudonym(conn_in, pseudonym_name_in):

    print pseudonym_name_in
    #return
    raise CustomException("Invalid FooFang")

def validate_date(date_in):

    try:
        x = time.strptime(date_in, '%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        raise CustomException("{NFP-Error-Code:{4002:ncorrect data format, should be %Y-%m-%dT%T.%f}}")

    return




