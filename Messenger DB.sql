CREATE DATABASE Messenger_DB;

USE Messenger_DB;

CREATE TABLE login_info (
	info_id VARCHAR(30) NOT NULL,
    info_pw VARCHAR(30) NOT NULL,
    id INT(11) AUTO_INCREMENT,
    PRIMARY KEY (id)
);

INSERT INTO login_info (info_id,info_pw) VALUES ("Admin","0000");
INSERT INTO login_info (info_id,info_pw) VALUES ("Test","Test");

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

INSERT INTO messages (title,message,send_date,sender,receiver,ischeck) VALUES ("Test1","It's First Test message",NOW(),"Test","Admin",False);
INSERT INTO messages (title,message,send_date,sender,receiver,ischeck) VALUES ("Test2","It's Second Test message",NOW(),"Test","Admin",False);