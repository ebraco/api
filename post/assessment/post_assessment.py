#!/usr/bin/python
import sys
import logging
import pymysql
import json
import boto
import nfp_validate

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    rawdata=json.dumps(event)
    reqid=context.aws_request_id
    environment=event["context"]["stage"]
   
    if environment == 'Beta':
        import rds_proto_config
        keyId  = rds_proto_config.keyId
        sKeyId  = rds_proto_config.sKeyId
        rds_host  = rds_proto_config.db_endpoint
        name = rds_proto_config.db_username
        password = rds_proto_config.db_password
        db_name = rds_proto_config.db_name
        port = 3306

    elif environment == 'dev':
        import rds_dev_config
    else:
        raise Exception('"NFP-Error-Code:No Environment Configured in Context"')

    try:
        conn = pymysql.connect(rds_host, user=name,
                           passwd=password, db=db_name, connect_timeout=10)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

    # Validate every pseudonym
    for pseudonym_row in event['body-json']['Pseudonym_Responses']:
        nfp_validate.validate_pseudonum(conn,pseudonym_row['Pseudonym_Response'])


    #Connect to S3 with access credentials
    conn = boto.connect_s3(keyId,sKeyId)
    bucket = conn.get_bucket('api-nfp')
    from boto.s3.key import Key

    #Get the Key object of the bucket
    k = Key(bucket)

    #Crete a new key with id as the name of the file
    k.key=reqid+".assessment.apigateway.json"

    #Upload the file
    result = k.set_contents_from_string(rawdata)

