import pymysql

conn = pymysql.connect(host='localhost', user='root', password='apmsetup',db='messenger_db', charset='utf8')
curs = conn.cursor()
sql = "select * from login_info"
curs.execute(sql)
rows = curs.fetchall()
print(rows)
conn.close()