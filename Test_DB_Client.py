import socket

print("Test Messenger Client")
userName = input("Input User Name  : ")
HOST = input("Input IP : ")
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connected to " + HOST)
s.sendall(userName.encode())

while True :
	command = input("Input User Name  : ")

s.close()
print ("Received" +  repr(data))