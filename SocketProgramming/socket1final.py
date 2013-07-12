from socket import *
from time import sleep
from threading import Thread

def threaded_function(channel, details):
    print("Received Connection:", details[0])
    try:
        message = channel.recv(1024)
        print(message)
        
        filename = message.split()[1]
        print(filename[1:])
        f = open(filename[1:])
        f.seek(0)
        outputdata = f.read()
        print(outputdata)

        #Send one HTTP header line into socket
        #Fill in start
        header = "HTTP/1.1 200 OK\r\n"
        channel.send(bytes(header, 'UTF-8'))
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            channel.send(bytes(outputdata[i], 'UTF-8')) # This line was modified to comply with Python 3x
        channel.close()

    except IOError:
        #Send response message for file not found
        #Fill in start
        """
        pageNotFound = "\r\nHTTP/1.1 404 Not Found\r\n\r\n"
        channel.send(bytes(pageNotFound, 'UTF-8'))


        """ #The following also works if you want to customize page:
        pageNotFound = "404.html"
        f = open(pageNotFound)
        outputdata = f.read()

        for i in range(0, len(outputdata)):
            channel.send(bytes(outputdata[i], 'UTF-8')) # This line was modified to comply with Python 3x
        channel.close()
        
        #Fill in end

        #Close client socket
        #Fill in start
        channel.close()
        #Fill in end

        



#-----------------------------------------------------
#Main Program
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverPort = 8001
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server is ready to receive")


while True:
    #Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    thread = Thread(target = threaded_function, args = (connectionSocket, addr))
    thread.start()

serverSocket.close()
