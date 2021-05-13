import socket
import struct
import time
import random

mbed_ip = "192.168.8.20"
SEND_PORT = 5555
mbed_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

## In case of broadcasting
# mbed_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAS, 1)

## Send string
# msg = "message from sender" 

## Send int
i = 0
data = i

while True:

	## Send string
	# msg = "Message from sender with random {:d}".format(random.randint(1,100))
	# mbed_sock.sendto(msg.encode('utf-8'),("192.168.8.20",SEND_PORT))

	## Send interger
	data = i
	print("python send ", data)
	data_pack = struct.pack("H", data)
	mbed_sock.sendto(data_pack, (mbed_ip, SEND_PORT))
	i += 1
	time.sleep(0.1)