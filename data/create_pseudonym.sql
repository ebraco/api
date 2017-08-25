drop table pseudonym;

create table pseudonym
(
pseudonym_id integer key not null AUTO_INCREMENT,
pseudonym_name varchar(256) not null,
start_date datetime not null,
end_date datetime null,
datatype varchar(32) not null,
default_question varchar(1024) null,
description varchar(1024) null
);
