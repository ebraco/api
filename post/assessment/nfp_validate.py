#!/usr/bin/python

def validate_pseudonym(conn_in, pseudonym_name_in):

    with conn_in.cursor() as cur:
       cur.execute('select pseudonym_name from pseudonym where pseudonym_name = %s', (pseudonym_name_in))
       if cur.rowcount == 0:
           error = "NFP-Error-Code:4001:Pseudonym (" + pseudonym_name_in + ")"
           raise Exception(error)
       else:
           return

    return

