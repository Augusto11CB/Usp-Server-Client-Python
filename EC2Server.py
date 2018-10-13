import socket
from threading import Thread
from SocketServer import ThreadingMixIn

TCP_IP = socket.gethostbyaddr("your-ec2-public_ip")[0]
TCP_IP = socket.gethostbyaddr("127.0.0.1")
TCP_PORT = 2222
BUFFER_SIZE = 1024

print('TCP_IP = ',TCP_IP)
print('TCP_PORT = ',TCP_PORT)

class ClientThread(Thread):

    def __init__(self, ip, port, sock):
        Thread.__init__(self):
        self.ip = ip
        self.port = port
        self.sock = sock
        print("New Thread Started For IP: " + ip + " -- Port: " + str(port))

    def run (self):
        filename = "mytext.txt"
        f = open(filename, 'rb')
        while (True):
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                print('Sent: ' + repr(l))
                l = f.read(BUFFER_SIZE)
                if not l:
                    f.close()
                    self.sock.close()
                    break


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((TCP_IP, TCP_PORT))

myThreads = []

while (True):
    mySocket.listen(5)
    print("Waiting for incoming connections...")
    conn, (ip,port) = mySocket.accept()
    print("Got connection from: " + str(ip) + " " + str(port))
    newThread = ClientThread(ip,port,conn)
    newThread.start()
    myThreads.append(newThread)

for t in myThreads:
    t.join()



