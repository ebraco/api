#!/usr/bin/python
import time

class NFP_Exception(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)


def validate_pseudonym(conn_in, pseudonym_name_in):

    with conn_in.cursor() as cur:
       cur.execute('select pseudonym_name from pseudonym where pseudonym_name = %s', (pseudonym_name_in))
       if cur.rowcount == 0:
           error = "{NFP-Error-Code:{4001:Pseudonym Not Valid (" + pseudonym_name_in + ")}}"

           raise NFP_Exception(error)
       else:
           return

    return

def validate_date(date_in):

    try:
        time.strptime(date_in, '%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        raise NFP_Exception("{NFP-Error-Code:{4002:Incorrect data format, should be YYYY-DD-MMTHH24:MI:SS.mmmmmmm}}")

    return
