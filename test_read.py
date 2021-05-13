import socket
import struct

PORT = 6666
data_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data_socket.bind(("0.0.0.0", PORT))
data_socket.setblocking(0)

while True:

	try:
		pkt, addr = data_socket.recvfrom(1024)
	except socket.error:
		pass
	else:
		# print(pkt)

		## in case of numbers
		# ! for network byte border (big-endian)
		parse_data = struct.unpack("!H", pkt)
		print("python recv", parse_data[0])

