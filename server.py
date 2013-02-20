#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
class Server:
 host='ctu-99-1'
 path='logs/ctu'
 filename='common-error.log'
 user='admin'
 password='alipay'
 def _init_(self):pass

def getserverlist():
 filename = 'server.txt'
 fileHandle = open(filename,'r')
 serverlist = []
 for line in fileHandle:
  conf = line.split(',')
  server = Server()
  server.host = conf[0]
  server.path = conf[1]
  server.filename = conf[2]
  server.user=conf[3]
  server.password=conf[4]
  serverlist.append(server)
 return serverlist
