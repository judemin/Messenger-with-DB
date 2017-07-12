'''
python Test_DB_Client.py
'''
import socket

print("Test Messenger Client")
HOST = input("Input IP : ")
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connected to " + HOST)

while True :
	print("")
	tmp = input("1:Login 2:Register - ")
	if tmp is '1':
		s.sendall(tmp.encode())
		tmp_id = input("Input ID : ")
		s.sendall(tmp_id.encode())
		tmp_pw = input("Input PW : ")
		s.sendall(tmp_pw.encode())
		status = (s.recv(1024)).decode('utf-8')
		if status is '1' :
			print("Welcome " + tmp_id)
			break
		else :
			print("ID or PW is Incorrect!")

	elif tmp is '2':
		s.sendall(tmp.encode())
		tmp_id = input("Input ID : ")
		s.sendall(tmp_id.encode())
		tmp_pw = input("Input PW : ")
		s.sendall(tmp_pw.encode())
		status = (s.recv(1024)).decode('utf-8')
		if status is '1' :
			print("Registration Complete!")
		else :
			print("Registration Error!")
	else:
		print("Incorrect Command")

s.close()