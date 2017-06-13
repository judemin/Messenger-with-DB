import pymysql
import socket

print("Test_DB_Server")
print("Connecting to Database")
ID='root'
PW = 'apmsetup'
DB = 'messenger_db'
conn = pymysql.connect(host='localhost', user=ID, password=PW,db=DB, charset='utf8')
curs = conn.cursor()
print("Successfully Connected to " +  DB)

print("Server Socket Listening")
HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ("Connected by " + addr[0])
data = conn.recv(1024)
stringdata = data.decode('utf-8')
print("UserName : " + stringdata)
conn.close()

while True :
	sql = input("Input Query : ")
	curs.execute(sql) 
	rows = curs.fetchall()
	print(rows)
conn.close()