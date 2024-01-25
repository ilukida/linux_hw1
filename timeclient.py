#!/usr/bin/env python3
import socket

server_ip = input("Input server IP: ")

client = socket.socket(
	socket.AF_INET, socket.SOCK_STREAM
) 

try:
	client.connect((server_ip, 1303))
	date = client.recv(1024).decode('utf-8')
	print('Current date: {date}')

except Exception as e:
    print("Error while connecting/receiving: {e}")

finally:
	client.close()