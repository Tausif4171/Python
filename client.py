#NAME : TAUSIF KHAN 
#SUBJECT: OSTL
#STD: SE COMPS(B)
#ROLL NO: 12
#EXPERIMENT NO: 10

import socket
host = '127.0.0.1'
port = 8000

#create a client side socket
s= socket.socket()
s.connect((host,port))

#enter data at client
str= input("Enter data: ")

#continue as long as exit not entered by user
while str!='exit':
    #send data from client to server
    s.send(str.encode())

    #receive the response data from server
    data = s.recv(1024)
    data = data.decode()
    print("from server: "+data)

    #enter data
    str=input("enter data: ")

s.close()
