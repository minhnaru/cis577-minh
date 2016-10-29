#--------------------------------------------------------
# Name: Minh Nguyen
# Student ID: 01597092
# CIS 577: SMTP with SSL
# Date Create: Oct 23, 2016
# Professor: Paul Gracia
#--------------------------------------------------------

import socket
import ssl
import base64
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

img = open("umass_logo.png", 'rb').read()
msgImg = MIMEImage(img, name=os.path.basename("umass_logo.png"))
msgImg.add_header('Content-ID', '<image>')

msgRoot = MIMEMultipart('related')

msg = MIMEText('\r\n I love computer networks!<br/>', 'html')
endmsg = "\r\n.\r\n"

msgRoot.attach(msg)
msgRoot.attach(msgImg)

recipient = '<tnguyen28@umassd.edu>'
sender = '<minhwhale@gmail.com>'
username = 'minhwhale'
password = 'minhnguyen123'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.gmail.com', 587)

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

# Request an encrypted connection
startTlsCommand = 'STARTTLS\r\n'
clientSocket.send(startTlsCommand)
tls_recv = clientSocket.recv(1024)
print tls_recv
if tls_recv[:3] != '220':
	print '220 reply not received from server'

# Encrypt the socket
ssl_clientSocket = socket.ssl(clientSocket)

# Send the AUTH LOGIN command and print server response.
authCommand = 'AUTH LOGIN\r\n'
ssl_clientSocket.write(authCommand)
auth_recv = ssl_clientSocket.read(1024)
print auth_recv
if auth_recv[:3] != '334':
	print '334 reply not received from server'

# Send username and print server response.
uname = base64.b64encode(username) + '\r\n'
ssl_clientSocket.write(uname)
uname_recv = ssl_clientSocket.read(1024)
print uname_recv
if uname_recv[:3] != '334':
	print '334 reply not received from server'

# Send password and print server response.
pword = base64.b64encode(password) + '\r\n'
ssl_clientSocket.write(pword)
pword_recv = ssl_clientSocket.read(1024)
print pword_recv
if pword_recv[:3] != '235':
	print '235 reply not received from server'

# Send MAIL FROM command and print server response.
mailfromCommand = 'MAIL FROM: ' + sender + '\r\n'
ssl_clientSocket.write(mailfromCommand)
recv1 = ssl_clientSocket.read(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Send RCPT TO command and print server response.
rcpttoCommand = 'RCPT TO: ' + recipient + '\r\n'
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
ssl_clientSocket.write(msgRoot.as_string())

# Message ends with a single period.
ssl_clientSocket.write(endmsg)
recv1 = ssl_clientSocket.read(1024)
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
