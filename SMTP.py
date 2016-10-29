#--------------------------------------------------------
# Name: Minh Nguyen
# Student ID: 01597092
# CIS 577: SMTP
# Date Create: Oct 23, 2016
# Professor: Paul Gracia
#--------------------------------------------------------

import socket

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('localhost', 25)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket.socket()
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
   print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
mailfromCommand = 'MAIL FROM: nguyenminhnaru@gmail.com\r\n'
ssl_clientSocket.write(mailfromCommand)
recv1 = ssl_clientSocket.read(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Send RCPT TO command and print server response.
rcpttoCommand = 'RCPT TO: tnguyen28@umassd.edu\r\n'
ssl_clientSocket.write(rcpttoCommand)
recv1 = ssl_clientSocket.read(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
ssl_clientSocket.write(dataCommand)
recv1 = ssl_clientSocket.read(1024)
print recv1
if recv1[:3] != '354':
    print '354 reply not received from server.'

# Send message data.
ssl_clientSocket.send(msg)

# Message ends with a single period.
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
ssl_clientSocket.write(quitCommand)
recv1 = ssl_clientSocket.read(1024)
print recv1
if recv1[:3] != '221':
    print '221 reply not received from server.'
print 'Mail Sent.'

clientSocket.close()
