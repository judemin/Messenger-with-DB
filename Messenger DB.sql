CREATE DATABASE Messenger_DB;

USE Messenger_DB;

CREATE TABLE login_info (
	info_id VARCHAR(30) NOT NULL,
    info_pw VARCHAR(30) NOT NULL,
    id INT(11) AUTO_INCREMENT,
    PRIMARY KEY (id)
);

INSERT INTO login_info (info_id,info_pw) VALUES ("Admin","0000");