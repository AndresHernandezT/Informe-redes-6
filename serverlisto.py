import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',50017))
s.listen(4)

def run(sock, addr):
	name = sock.recv(1024)
	print name, "acaba de conectarse."
	while True:
		message = sock.recv(1024)
		print name + ':', message
		if message == "salir":
			break
	sock.close()

print('~Server iniciado~')
while True:
	sock, addr = s.accept()
	t = threading.Thread(target = run, args = (sock, addr))
	t.start()

s.close()