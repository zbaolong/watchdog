#!/usr/bin/python
# _*_ coding:utf-8 _*_

import re
import paramiko

import keyfactor
import errorinfo
import loglist

def analyze():
    serverlist = loglist.getloglist()
    for s in serverlist:
        host = s.host
        path = s.path
        filename = s.filename
        username = s.user
        password = s.password
        print host + username + password
        analyzeSignal(host, path, filename, username, password)

def analyzeSignal(host, path, filename, username, password):
    port = 22
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.chdir(path)
    fileHandle = sftp.open(filename, 'r')
    keylist = []
    switch = False
    content = ''
    for line in fileHandle:
        timefmt = '[0-9]{4}-[01][0-9]-[0-3][0-9] [0-2][0-9]:[0-5][0-9]:[0-5][0-9]'
        head = re.match(timefmt, line)
        if head:
            allwords = re.split(r'\s+', line)
            key = allwords[3]
            
            it = iter(keylist)
            exist = False
    
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
                factor.first_time = allwords[1]
                factor.last_time = allwords[1]
                factor.time_list.append(allwords[1])
                keylist.append(factor)

                switch = True
                content = content + line

            else:
                factor.last_time = allwords[1]
                factor.time_list.append(allwords[1])
        else:
            if switch == True:
                content = content + line

    fileHandle.close()
    transport.close()
    errorinfo.recordError(host, keylist, content)
