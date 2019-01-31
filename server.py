#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
serverSocket.bind(("", 8080)) # bind to localhost
serverSocket.listen(5) # set the socket to listen

#max packet size to receive
PACKET_SIZE = 1024

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept()

    print("Client connected: ",addr)

    data = connectionSocket.recv(PACKET_SIZE).decode()
    print("data[0]:",data)

    data = data.split(' ')
    

    if data[0] == "GET":
        print("Get request received.")

        requestedFile = data[1]
       
 
        try:
            if requestedFile == "/":
                requestedFile = "hello.html"     

            #get rid of the /
            requestedFile = requestedFile.strip('/')
            print("requestedFile:",requestedFile)
            f = open(requestedFile, 'r') 

            outputdata = f.read() 
            print(outputdata)               
        
            #Send response - header and html data.
            response = "HTTP/1.1 200 OK\n"
            response += "Content-Type: text/html\n\n"

            response += outputdata
            
            connectionSocket.send(response.encode('utf-8'))
            connectionSocket.close()

        except Exception:
            print("404 Not Found.")
            #Send response message for file not found
            response = "HTTP/1.1 404 Not Found\n"
            response += "<html><body><center><h1>Error 404: File not found</h1></center><p>Head back to dry land.</p></body></html>"
            connectionSocket.send(response.encode('utf-8'))
            print("sent 404.")
            connectionSocket.close()

    else:
        print("Unknown HTTP request method encountered.")
        connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
