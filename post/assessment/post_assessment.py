#!/usr/bin/python
import sys
import logging
import pymysql
import json
import boto

def lambda_handler(event, context):
    
    rawdata=json.dumps(event)
    reqid=context.aws_request_id
    environment=event["context"]["stage"]
   
    if environment == 'Beta':
       import rds_proto_config
       keyId  = rds_proto_config.keyId
       sKeyId  = rds_proto_config.sKeyId
    elif environment == 'dev':
       import rds_dev_config
    else:
       raise Exception('"NFP-Error-Code:No Environment Configured in Context"')

    #keyId = "AKIAJ76RR3BYTOPWPFUQ"
    #sKeyId="TiHi8LVgSprJHt5H44ijedaGuZECFz0sRJ8dARvA"
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

