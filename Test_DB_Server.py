import pymysql

print("Test_DB_Server")
ID='root'
PW = 'apmsetup'
DB = 'messenger_db'
conn = pymysql.connect(host='localhost', user=ID, password=PW,db=DB, charset='utf8')
curs = conn.cursor()
while True :
	sql = input("Input Query : ")
	curs.execute(sql)
	rows = curs.fetchall()
	print(rows)
conn.close()