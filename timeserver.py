#!/usr/bin/env python3
import socket
from datetime import datetime

server = socket.socket(
	socket.AF_INET, socket.SOCK_STREAM
)

server.bind(
	('192.168.56.104', 1303)
)

server.listen(1)

while True:
	user, addr = server.accept()
	print("CONNECTED:{user} /n {addr}")

	try:
		date = datetime.now().strftime("%d.%m.%Y %H:%M")
		user.send(date.encode('utf-8'))

	except Exception as e:
        print("Error while sending: {e}")
	
	finally:
		user.close()
