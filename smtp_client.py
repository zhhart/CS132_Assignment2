#Zachary Hart 70953123
#Daniel Lara 49651280
from socket import *

senderAddress = 'laraD@uci.edu'
rcptAddress = 'zhhart@uci.edu'

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
#This is considered optional. 

mailserver = 'localhost'
mailport = 25

# Create socket called clientSocket and establish a TCP connection with mailserver

#SECTION COMPLETE
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailport))

recv = clientSocket.recv(1024).decode()

print(recv)

if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')
 


# Send MAIL FROM command and print server response.
#SECTION COMPLETE
mailFromCmd = 'MAIL FROM: ' + senderAddress + '\r\n'
clientSocket.send(mailFromCmd.encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')



# Send RCPT TO command and print server response.
#SECTION COMPLETE
rcptToCmd = 'RCPT TO: ' + rcptAddress + '\r\n'
clientSocket.send(rcptAddress.encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')



# Send DATA command and print server response.
#SECTION COMPLETE
dataCmd = 'DATA\r\n'
clientSocket.send(dataCmd.encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
#SECTION COMPLETE
msgCmd = msg
# Message ends with a single period.
endMsgCmd = endmsg
clientSocket.send((msgCmd + endMsgCmd).encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')



# Send QUIT command and get server response.
#SECTION COMPLETE
quitCmd = 'QUIT\r\n'
clientSocket.send(quitCmd.encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '221':
    print('221 reply not received from server.')