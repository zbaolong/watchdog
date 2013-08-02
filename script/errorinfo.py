#!/usr/bin/python
# _*_ coding:utf-8 _*_

import os
import time
import keyfactor

#get current time
def now():
  return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

# write common-error information into the file
def recordError(host,keylist,content):
  time = now();
  path = '../result/'
  if not os.path.exists(path):
   os.makedirs(path)
  
  errorname = path + host + '-' + time + '-' + 'stat.txt'
  errorinfo = open(errorname,'w+')
  length = len(keylist)
  it = iter(keylist)
  factor = keyfactor.KeyFactor()
  try:
     while True:
       factor = it.next()
       line = factor.keyWord + ':' + str(factor.keyCount) + '\n'
       errorinfo.write(line)
  except StopIteration:
     pass
  finally:
     errorinfo.close()
  
  contentname = path + host + '-' + time + '-' + 'content.txt'
  contentinfo = open(contentname,'w')
  try:
     contentinfo.write(content)
  finally:
     contentinfo.close()
