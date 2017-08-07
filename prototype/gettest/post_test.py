#!/usr/bin/python
import sys
import logging
import rds_config
import pymysql
import json
import boto

def lambda_handler(event, context):
    data=json.dumps(event)

    keyId = "AKIAJ76RR3BYTOPWPFUQ"
    sKeyId="TiHi8LVgSprJHt5H44ijedaGuZECFz0sRJ8dARvA"
    #Connect to S3 with access credentials 
    conn = boto.connect_s3(keyId,sKeyId) 
    bucket = conn.get_bucket('api-nfp')
    from boto.s3.key import Key
    
    #Get the Key object of the bucket
    k = Key(bucket)
    
    #Crete a new key with id as the name of the file
    k.key="nurse.json.api"
    
    #Upload the file
    result = k.set_contents_from_string(data)
    #result contains the size of the file uploaded
    
    #print json_data
    #print data["Ethnicity"]
    
    #for element in data['Race']:
    #    print element
    
    #print json.dumps(data, sort_keys=True, indent=4)





