#!/usr/bin/python
import sys
import logging
import rds_config
import pymysql
import json
import boto

file="./get.json"
json_data=open(file).read()

data=json.loads(json_data)

print data["params"]["querystring"]["Assessment"]





