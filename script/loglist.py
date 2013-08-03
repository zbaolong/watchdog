#!/usr/bin/python
# _*_ coding:utf-8 _*_

import log

# 获取所有待分析的日志列表,并校验信息是否合法
def getloglist():
    
    filename = '../conf/server.txt'
    fileHandle = open(filename, 'r')
    
    loglist = []
    for line in fileHandle:
        conf = line.split(',')
        length = len(conf)
        if(length >= 5):
            try:
                ser = log.LOG()
                ser.host = conf[0]
                ser.path = conf[1]
                ser.filename = conf[2]
                ser.user = conf[3]
                ser.password = conf[4]
                loglist.append(ser)
            except IndexError:
                print "list index out of range!" 
        else:
            print line + " Error, information is not enough!"
    
    fileHandle.close();
    
    return loglist