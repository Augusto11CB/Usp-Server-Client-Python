#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #is used to associate the socket with a specific network interface and port number:
    s.bind((HOST, PORT))
    #listen() has a backlog parameter. It specifies the number of unaccepted connections 
                # that the system will allow before refusing new connections.
    s.listen()
    #accept() blocks and waits for an incoming connection. When we have a connection accept()
                #returns a new socket object representing the connection and a tuple holding the client adress
    conn, addr = s.accept() # The tuple will contain (host, port) for IPv4 connections or (host, port, flowinfo, scopeid)
    with conn: # conn is the new socket that we use to communicate with the client
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)