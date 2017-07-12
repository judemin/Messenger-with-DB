'''
python Test_DB_Server.py
'''
import pymysql
import socket

print("Test_DB_Server")
print("Connecting to Database")
ID='root'
PW = 'apmsetup'
DB = 'messenger_db'
table = 'login_info'
connDB = pymysql.connect(host='localhost', user=ID, password=PW,db=DB, charset='utf8')
curs = connDB.cursor()
print("Successfully Connected to " +  DB)

print("Server Socket Listening")
HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ("Connected by " + addr[0])

while True :
	data = (conn.recv(1024)).decode('utf-8')
	if data is '1':
		print("Login request")
		isLogin = False
		tmp_id = (conn.recv(1024)).decode('utf-8')
		print("Received ID : " + tmp_id)
		tmp_pw = (conn.recv(1024)).decode('utf-8')
		print("Received PW : " + tmp_pw)
		curs.execute("SELECT * FROM " + table) 
		row = curs.fetchone()
		while row is not None :
			if (tmp_id == row[0]) and (tmp_pw == row[1]) :
				isLogin = True
				break
			row = curs.fetchone()
		if isLogin is True : 
			tmpM = '1'
			conn.sendall(tmpM.encode())
			print("Login Complete from " + tmp_id)
			break
		else :
			tmpM = '0'
			conn.sendall(tmpM.encode())
			print("Login Error from " + tmp_id)

	if data is '2':
		print("Registration request")
		canCreate = True
		tmp_id = (conn.recv(1024)).decode('utf-8')
		print("Received ID : " + tmp_id)
		tmp_pw = (conn.recv(1024)).decode('utf-8')
		print("Received PW : " + tmp_pw)
		curs.execute("SELECT * FROM " + table) 
		row = curs.fetchone()
		while row is not None :
			if tmp_id == row[0] :
				canCreate = False
				break
			row = curs.fetchone()
		if canCreate is True : 
			print("Inserting Data to DB...")
			curs.execute("INSERT INTO " + table + " (info_id,info_pw) VALUES (%s,%s)", 
			  (tmp_id,tmp_pw))
			connDB.commit()
			print("Commit Complete!")
			tmpM = '1'
			conn.sendall(tmpM.encode())
			print("Registration Complete from " + tmp_id)
		else :
			tmpM = '0'
			conn.sendall(tmpM.encode())
			print("Registration Error from " + tmp_id)

conn.close()