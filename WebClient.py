#--------------------------------------------------------# Name: Minh Nguyen# Student ID: 01597092# CIS 577: Socket Web Server# Date Create: Oct 23, 2016# Professor: Paul Gracia#--------------------------------------------------------#import socket modulefrom socket import *import sysserverHost = sys.argv[1]serverPort = int(sys.argv[2])filename = sys.argv[3]hostport = "%s:%s" %(serverHost, serverPort)try:     clientSocket = socket(AF_INET, SOCK_STREAM)     clientSocket.connect((serverHost, (serverPort)))     header = {          "firstheader" : "GET /%s HTTP/1.1" %(filename),          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",          "AcceptLanguage": "en-us",          "Host": hostport,          }     http_header = "\r\n".join("%s:%s" %(item,header[item]) for item in header)     print http_header     clientSocket.send("%s\r\n\r\n" %(http_header))except (IOError, IndexError):     sys.exit(1)     print "404 Not Found"final = ""response_msg = clientSocket.recv(1024)while response_msg:     final += response_msg     response_msg = clientSocket.recv(1024)clientSocket.close()print final