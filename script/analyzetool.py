#!/usr/bin/python
# _*_ coding:utf-8 _*_

import re
import paramiko
import time

import keyfactor
import errorinfo

def analyze(host, path, filename, username, password, port):
    
    print 'start to analyze ' + host + '-' + filename + '\n'
    start = time.time()
    
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.chdir(path)
    fileHandle = sftp.open(filename, 'r')
    dowords(fileHandle, host, filename)
    fileHandle.close()
    transport.close()
    
    end = time.time();
    print 'finished to analyze' + host + '-' + filename
    print ',total time is %f \n' % (end - start)
    
def getheadwords(line):
    return re.split(r'\s+', line)

def getkey(line):
    allwords = getheadwords(line)
    if allwords[2] == 'ERROR':
        return allwords[3]
    elif allwords[5] == 'ERROR':
        return allwords[6]
    else:
        print 'the line is ' + line
        print 'Error, can\'t find any error!'
        

def gettime(line):
    allwords = getheadwords(line)
    return (allwords[0] + ' ' + allwords[1])
    
def dowords(fileHandle, host, filename):
    keylist = []
    switch = False
    content = ''
    for line in fileHandle:
        timefmt = '[0-9]{4}-[01][0-9]-[0-3][0-9] [0-2][0-9]:[0-5][0-9]:[0-5][0-9]'
        # start = time.time()
        head = re.match(timefmt, line)
        # end = time.time()
        # print 'math spends %f \n' % (end - start) 
        
        if head:
            # start = time.time()
            key = getkey(line)
            # end = time.time()
            # print 'split spends %f \n' % (end - start)
            it = iter(keylist)
            exist = False
            
            # start = time.time()
            switch = False
            try:
                while True: 
                    factor = it.next()
                    if cmp(factor.key_word, key) == 0:
                        factor.key_count = factor.key_count + 1
                        exist = True
            except StopIteration:
                pass
            if exist == False:
                factor = keyfactor.KEYFACTOR()
                factor.key_word = key
                factor.key_content = line
                factor.key_count = 1
                factor.first_time = gettime(line)
                factor.last_time = gettime(line)
                factor.time_list.append(gettime(line))
                keylist.append(factor)

                switch = True
                content = content + line

            else:
                factor.last_time = gettime(line)
                factor.time_list.append(gettime(line))
        else:
            if switch == True:
                content = content + line
                # factor.key_content = factor.key_content + line;
        # end = time.time()
        # print 'keyfactor spends %f \n' % (end - start)
    errorinfo.recordError(host, keylist, content)
