#!/usr/bin/python
# _*_ coding:utf-8 _*_

import os
import time
import keyfactor

# get current time
def now():
    return time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

# write common-error information into the file
def recordError(host, keylist, content):
    time = now();
    path = '../result/'
    if not os.path.exists(path):
        os.makedirs(path)
    
    pubname = path + host + '-' + time + '-'
    indexname = pubname + 'index.txt'
    detailname = pubname + 'detail.txt'
    timename = pubname + 'time.txt'
    
    indexinfo = open(indexname, 'w+')
    detailinfo = open(detailname, 'w+')
    timeinfo = open(timename, 'w+')
    it = iter(keylist)
    factor = keyfactor.KEYFACTOR()
    try:
        while True:
            factor = it.next()
            
            index = 'keyword:' + factor.key_word + '\nkeycount:' + str(factor.key_count) + '\nfirsttime:' + factor.first_time + '\nlasttime:' + factor.last_time + "\n";
            indexinfo.write(index)
            
            detail = index + "keycontent:" + factor.key_content + '\n'
            detailinfo.write(detail)
            
            alltime = ''
            for t in factor.time_list:
                alltime = alltime + t + '\n'
            time = index + "timelist:" + alltime + "\n"
            timeinfo.write(time)
            
    except StopIteration:
        pass
    finally:
        indexinfo.close()
        detailinfo.close()
        timeinfo.close()
