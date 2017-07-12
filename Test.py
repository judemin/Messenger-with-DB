import pymysql
import socket

print("MySQL Test Code")
print("Connecting to Database")
ID='root'
PW = 'apmsetup'
DB = 'messenger_db'
table = 'login_info'
conn = pymysql.connect(host='localhost', user=ID, password=PW,db=DB, charset='utf8')
curs = conn.cursor()
print("Successfully Connected to " +  DB)
curs.execute("SELECT * FROM " + table) 
row = curs.fetchone()
while row is not None:
	print(row[0] + " " + row[1])
	row = curs.fetchone()

conn.close()