#!/usr/bin/python
import sys
import rds_config
import pymysql
import json

rds_host  = rds_config.db_endpoint
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name
port = 3306


try:
    conn = pymysql.connect(rds_host, user=name,
                           passwd=password, db=db_name, connect_timeout=5)
except:
    print("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

    """
    This function inserts content into mysql RDS instance
    """
item_count = 0
data='{'
with conn.cursor() as cur:
    cur.execute("select * from pseudonym")
    rows = cur.fetchall()

    for row in rows:
       data=data+'"pseudonym_name" : "'+row[1]+'"'

data=data+"}"
print(data)
