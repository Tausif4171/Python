#NAME : TAUSIF KHAN 
#SUBJECT: OSTL
#STD: SE COMPS(B)
#ROLL NO: 12
#EXPERIMENT NO: 10

import socket
host = '127.0.0.1'
port = 8000

#create server side socket
s= socket.socket()
s.bind((host,port))
#let maximum number of connections are 1 only
s.listen(2)

#wait till a client connects
c, addr = s.accept()
print("A Client Connected")

#server runs continously
while True:
    #receive data from client
    data= c.recv(1024)

    #if client sends empty string, come out
    if not data:
        break
    print("from client: "+str(data.decode()))

    #enter response data from server
    data1 = input("Enter response: ")

    #send that data to client
    c.send(data1.encode())

#close connection
c.close()
    
    
    
