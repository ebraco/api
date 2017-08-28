#!/usr/bin/python

def validate_pseudonym(conn_in, pseudonym_name_in):

    with conn_in.cursor() as cur:
       cur.execute('select pseudonym_name from pseudonym where pseudonym_name = %s', (pseudonym_name_in))

    return

