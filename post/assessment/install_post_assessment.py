#!/bin/sh  -x
lambda_name="post_assessment"
zip_file="${lambda_name}.zip"
role_arn="arn:aws:iam::312517840624:role/Swaggerhub-FullAccess"
#subnet_ids=`aws ec2 describe-subnets |\
#                jq -r '.Subnets|map(.SubnetId)|join(",")'`
#sec_group_id=`aws ec2 describe-security-groups --group-name "default" |\
#                jq -r '.SecurityGroups[].GroupId'`
sec_group_id='sg-21b70f59'
subnet_ids='subnet-9aba62fd'

files="${labda_name}.py rds_proto_config.py rds_dev_config.py"
chmod 755 ${files}
zip -r "${zip_file}" pymysql boto ${files}

aws lambda delete-function \
    --region "us-west-2" \
    --function-name "${lambda_name}"

aws lambda create-function \
    --region "us-west-2" \
    --function-name "${lambda_name}"  \
    --zip-file "fileb://${zip_file}" \
    --role "${role_arn}" \
    --handler "${lambda_name}.lambda_handler" \
    --runtime python2.7 \
    --timeout 60 \
    --vpc-config SubnetIds="${subnet_ids}",SecurityGroupIds="${sec_group_id}"

