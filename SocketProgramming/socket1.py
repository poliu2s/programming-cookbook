#import socket module

from socket import *
from threading import Thread
from time import sleep 





serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
serverPort = 8001
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server is ready to receive")
#Fill in end


while True:
    #Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    print(connectionSocket)
    #help(connectionSocket)
    print(int(addr[1]))
    
    try:
        message = ""
        message = connectionSocket.recv(1024)
        print(message)
        
        filename = message.split()[1]
        print(filename[1:])
        f = open(filename[1:])
        outputdata = f.read()
        print(outputdata)

        #Send one HTTP header line into socket
        #Fill in start
        header = "HTTP/1.1 200 OK\r\n" #"Date: Friday, 12 October 2012 00:00:00 GMT\r\n"
        connectionSocket.send(bytes(header, 'UTF-8'))
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(bytes(outputdata[i], 'UTF-8')) # This line was modified to comply with Python 3x
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        #Fill in start
        pageNotFound = "404.html"
        f = open(pageNotFound)
        outputdata = f.read()

        for i in range(0, len(outputdata)):
            connectionSocket.send(bytes(outputdata[i], 'UTF-8')) # This line was modified to comply with Python 3x
        connectionSocket.close()
        #Fill in end

        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

serverSocket.close()
