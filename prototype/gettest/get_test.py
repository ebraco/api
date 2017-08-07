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

    item_count = 0
    with conn.cursor() as cur:
       cur.execute('select pseudonym_name, datatype, DATE_FORMAT(start_date, "%Y-%m-%dT%T.%f") as start_date, description from pseudonym')
       row_headers=[x[0] for x in cur.description]
       rv = cur.fetchall()
       json_data=[]
       for result in rv:
           json_data.append(dict(zip(row_headers,result)))

#print(data)

    return json_data
