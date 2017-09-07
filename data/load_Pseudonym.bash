#!/bin/bash

mysql --user="master" --password='NFP!2017!' --host=jdg-proto-type.ccf0v3myj6k1.us-west-2.rds.amazonaws.com --database=Dev << EOF
source create_pseudonym.sql

DELETE FROM pseudonym;

LOAD DATA LOCAL INFILE 'Pseudonym.csv'
INTO TABLE pseudonym
	FIELDS TERMINATED BY ','
		OPTIONALLY ENCLOSED BY '"'
	LINES  TERMINATED BY '\n'
(pseudonym_name, default_question)
SET pseudonym_id = NULL,
    start_date = str_to_date('01/01/2000','%m/%d/%Y');

exit
EOF
