#!/usr/bin/python
# _*_ coding:utf-8 _*_

import time
import keyfactor

#get current time
def now():
  return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

# write common-error information into the file
def recordError(host,keylist,content):
  time = now();
  errorname = host + time + 'count.txt'
  errorinfo = open(errorname,'w')
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

  contentname = host + time + 'content.txt'
  contentinfo = open(contentname,'w')
  try:
     contentinfo.write(content)
  finally:
     contentinfo.close()
