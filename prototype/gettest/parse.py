#!/usr/bin/python
import sys
import logging
import rds_config
import pymysql
import json
import boto
import validate

file="./test.json"
json_data=open(file).read()

data=json.loads(json_data)

#print data["body-json"]["Pseudonym_Responses"]

#for pseudonym_row in data['body-json']['Pseudonym_Responses']:
        ##print pseudonym_row['Pseudonym_Response']
    #try: 
        #validate.validate_pseudonym(1,pseudonym_row['Pseudonym_Response'])
    #except validate.CustomException, (instance):
        #print "Caught: " + instance.parameter

validate.validate_date(data["body-json"]["Assessment_Date"])






