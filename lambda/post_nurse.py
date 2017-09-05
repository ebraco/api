#!/usr/bin/python
import sys
import logging
import pymysql
import json
import boto
import nfp_validate
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
   
    #convert event from python var to string 
    rawdata=json.dumps(event)

    #grab the context request id for naming
    reqid=context.aws_request_id

    # grab the /Area the API is being called from aka the environment
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
        keyId  = rds_dev_config.keyId
        sKeyId  = rds_dev_config.sKeyId
        rds_host  = rds_dev_config.db_endpoint
        name = rds_dev_config.db_username
        password = rds_dev_config.db_password
        db_name = rds_dev_config.db_name
        port = 3306
    else:
        raise Exception('"NFP-Error-Code:No Environment Configured in Context"')

    try:
        conn = pymysql.connect(rds_host, user=name,
                           passwd=password, db=db_name, connect_timeout=30)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

    # Validate NFP_Start_Date
    try:
        nfpstartdate=event['body-json']['NFP_Start_Date']
        try:
            nfp_validate.validate_date(nfpstartdate)
        except nfp_validate.NFP_Exception, (instance):
            return(instance.parameter)
    except: 
        pass
    #try:
        #nfp_validate.validate_date(event['body-json']['Assessment_Date'])
    #except nfp_validate.NFP_Exception, (instance):
            #return(instance.parameter)


    #Connect to S3 with access credentials
    conn = boto.connect_s3(keyId,sKeyId)
    bucket = conn.get_bucket('api-nfp')
    from boto.s3.key import Key

    #Get the Key object of the bucket
    k = Key(bucket)

    #Crete a new key with id as the name of the file
    k.key=reqid+".nurse.apigateway.json"

    #Upload the file
    result = k.set_contents_from_string(rawdata)

    return('{message:success}')

