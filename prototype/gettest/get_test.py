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
    
    #data=json.loads(event)
    data=event
    qs=data["params"]["querystring"]["Assessment"]
    #qa=data["params"]
    #qs="ccc"    

    try:
        conn = pymysql.connect(rds_host, user=name,
                           passwd=password, db=db_name, connect_timeout=10)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

    item_count = 0
    with conn.cursor() as cur:
       cur.execute('select pseudonym_name as Pseudonym, datatype as Data_Type, DATE_FORMAT(start_date, "%Y-%m-%dT%T.%f") as Start_Date, description as Description from pseudonym')
       row_headers=[x[0] for x in cur.description]
       rv = cur.fetchall()
       json_data=[]
       for result in rv:
          json_data.append(dict(zip(row_headers,result)))
       
       if qs == "error": 
          raise Exception('"NFP-Error-Code:400059"')
       else:
          return json_data
