import socket

target_host = "127.0.0.1"
target_port = 80

#Creating socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto(b'this is test data',(target_host,target_port))

#Receive data
data,addr = client.recvfrom(4096)

print(data)