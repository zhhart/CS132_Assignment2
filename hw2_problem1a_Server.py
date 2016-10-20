#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)

#Maximum length of the pending connections queue
BACKLOG = 1

#HTTP HEADERS
# header identifies the program that's making the request, in the form "Program-name/x.xx", 
# where x.xx is the (mostly) alphanumeric version of the program. For example, 
# Netscape 3.0 sends the header "User-agent: Mozilla/3.0Gold".
# (Example taken from: http://www.jmarshall.com/easy/http/#headerlines)

# Standard response for successful HTTP requests. The actual response will depend on the request method used. 
# In a GET request, the response will contain an entity corresponding to the requested resource. 
# In a POST request, the response will contain an entity describing or containing the result of the action.
# (This description is from wikipedia https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#1xx_Informational)
HTTP_HEADER_OK = '\r\nHTTP/1.xx 200 OK\r\n'

# The requested resource could not be found but may be available in the future. 
# Subsequent requests by the client are permissible.
# (This description is from wikipedia https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#1xx_Informational)
HTTP_HEADER_NOTFOUND = '\r\nHTTP/1.xx 404 Not Found\r\n'

#Prepare a sever socket

#Section Complete
# Setup a specific port number
_serverPort = 6789
#Setup a specific Host name
_serverHost = 'LaHart'
#Bind both the Host and Port to the already setup Socket
serverSocket.bind(_serverHost, _serverPort)

# Place the socket in a listening state. Its passed in argument is the maximum length of pending connections
# For this assignment, we have been asked to accept one connection at a time.
serverSocket.listen(BACKLOG)

while True:
    #Establish the connection
    print('Ready to serve...')

    #Setup the client socket
    connectionSocket, addr = serverSocket.accept() #Line Complete
    try:
        message = connectionSocket.recv(1024) #Line Complete
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() #Line Complete

        #Send one HTTP header line into socket

        #Section Complete
        connectionSocket.send(HTTP_HEADER_OK)

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.send("\r\n".encode())

        #Close client socket
        connectionSocket.close()

    except IOError:
        #Send response message for file not found

        #Section Complete
        connectionSocket.send(HTTP_HEADER_NOTFOUND);
        connectionSocket.send('File doesn\'t exist on this server.\r\n')

        #Close client socket

        #Section Complete
        connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 
