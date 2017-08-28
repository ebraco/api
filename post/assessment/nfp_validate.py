#!/usr/bin/python

def validate_pseudonym(conn_in, pseudonym_name_in):

    with conn_in.cursor() as cur:
       cur.execute("select pseudonym_name as Pseudonym from pseudonym = %s", (pseudonym_name_in))
       row_headers=[x[0] for x in cur.description]
       rv = cur.fetchall()
       json_data=[]
       for result in rv:
          json_data.append(dict(zip(row_headers,result)))

       if qs == "error":
          raise Exception('"NFP-Error-Code:400059"')
       else:
          return json_data

    return

