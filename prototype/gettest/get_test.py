#!/usr/bin/python
import sys
import logging
import rds_config
import pymysql
import json

rds_host  = rds_config.db_endpoint
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name
port = 3306

logger = logging.getLogger()
logger.setLevel(logging.INFO)


logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
def lambda_handler(event, context):
    """
    This function inserts content into mysql RDS instance
    """
    try:
        conn = pymysql.connect(rds_host, user=name,
                           passwd=password, db=db_name, connect_timeout=5)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

    print("Hi AWS Support!")
    item_count = 0
    data='{'
    with conn.cursor() as cur:
        cur.execute("select * from pseudonym")
        rows = cur.fetchall()

        for row in rows:
            data=data+'"pseudonym_name" : "'+row[1]+'"'

    data=data+"}"
    return data
