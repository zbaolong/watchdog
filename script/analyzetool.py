#!/usr/bin/python
# _*_ coding:utf-8 _*_

import re
import sys
import paramiko
import keyfactor
import errorinfo
import server

def analyze():
 serverlist = server.getserverlist()
 for s in serverlist:
  host = s.host
  path = s.path
  filename = s.filename
  username = s.user
  password = s.password
  print host + username + password
  analyzeSignal(host,path,filename,username,password)

def analyzeSignal(host,path,filename,username,password):
 port = 22
 transport = paramiko.Transport((host,port))
 transport.connect(username = username,password = password)
 sftp = paramiko.SFTPClient.from_transport(transport)
 sftp.chdir(path)
 fileHandle = sftp.open(filename,'r')
 keylist = []
 switch = False
 content = ''
 for line in fileHandle:
  timefmt = '[0-9]{4}-[01][0-9]-[0-3][0-9] [0-2][0-9]:[0-5][0-9]:[0-5][0-9]'
  head = re.match(timefmt,line)
  if head:
   allwords= re.split(r'\s+',line)
   key = allwords[3]
   
   length = len(keylist)
   it = iter(keylist)
   exist = False

   switch = False
   try:
     while True: 
       factor = it.next()
       if cmp(factor.keyWord, key) == 0:
          factor.keyCount = factor.keyCount + 1
          exist = True
   except StopIteration:
     pass
   if exist == False:
     factor = keyfactor.KeyFactor()
     factor.keyWord = key
     factor.keyCount = 1
     keylist.append(factor)

     switch = True
     content = content + line

   else:
     pass
  else:
      if switch == True:
        content = content + line

 fileHandle.close()
 errorinfo.recordError(host,keylist,content)
 transport.close()
