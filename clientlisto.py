import socket
import threading

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1',50017))

name = raw_input("Ingrese nombre: ")
c.send(name)

def sending():
	while True:
		i = raw_input(name+': ')
		c.send(i)
		if i == "salir":
			c.send(i)
			break
	c.close()

t1 = threading.Thread(target = sending)
t1.start()