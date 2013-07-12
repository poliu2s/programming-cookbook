from socket import *
import time
from threading import Thread

#Thread
def threaded_function(pingSocket, pingNum):
    serverPort = 12000
    print("Thread ", pingNum, " running...")
    message = 'Ping '
    message += str(pingNum)
    message += "   "
    message += str(time.time())
    startTime = time.time()
    pingSocket.sendto(bytes(message, 'UTF-8'),
                        (bytes('127.0.0.1', 'UTF-8'),int(serverPort)))
    
    modifiedMessage, serverAddress = pingSocket.recvfrom(1024)
    endTime = time.time()

    #Calculation for milliseconds
    roundTT = int(1000*(endTime - startTime)) 
    print("Total RTT: ", roundTT, " milliseconds")
    print("Response: ", modifiedMessage.decode("UTF-8"))
    
    #Close the connection after printing
    pingSocket.close()



#Main Client Program
for i in range(0, 10):
    print("------")
    
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    print("Starting to ping...")
    fancyNum = i+1
    thread = Thread(target = threaded_function, args = (clientSocket,
                                                        fancyNum))
    thread.start()
    time.sleep(1)
    if thread.isAlive():
        print("Request timed out")

