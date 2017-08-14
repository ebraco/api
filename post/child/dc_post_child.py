#!/usr/bin/python
import sys
import logging
#import rds_config
import pymysql
import json
import boto
#import datetime

def lambda_handler(event, context):
    data=json.dumps(event)

    reqid=context.aws_request_id

    keyId = "AKIAJ76RR3BYTOPWPFUQ"
    sKeyId="TiHi8LVgSprJHt5H44ijedaGuZECFz0sRJ8dARvA"
    #Connect to S3 with access credentials 
    conn = boto.connect_s3(keyId,sKeyId) 
    bucket = conn.get_bucket('api-nfp')
    from boto.s3.key import Key
    
    #Get the Key object of the bucket
    k = Key(bucket)
    
    #Crete a new key with id as the name of the file
    #TODO
    # Add Data Source System.Agency ID
    #  if Null for either FAIL
    #  Add Date: YYYYMMDDHH24MISS.SSSSS.  Last
    #  DSS.AID.date.reqid.jsonobject.json
    #currentdt=datetime.datetime.now()
    k.key=reqid+".child.json"
    
    #Upload the file
    result = k.set_contents_from_string(data)
    #result contains the size of the file uploaded
    



