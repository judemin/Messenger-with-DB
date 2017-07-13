CREATE DATABASE Messenger_DB;

USE Messenger_DB;

CREATE TABLE login_info (
	info_id VARCHAR(30) NOT NULL,
    info_pw VARCHAR(30) NOT NULL,
    id INT(11) AUTO_INCREMENT,
    PRIMARY KEY (id)
);

INSERT INTO login_info (info_id,info_pw) VALUES ("Admin","0000");

CREATE TABLE messages(
	title VARCHAR(100) NOT NULL,
    message VARCHAR(1000) NOT NULL,
    send_date datetime NOT NULL,
    sender VARCHAR(30) NOT NULL,
    receiver VARCHAR(30) NOT NULL,
    ischeck bool NOT NULL,
    id INT(11) AUTO_INCREMENT,
    PRIMARY KEY (id)
);