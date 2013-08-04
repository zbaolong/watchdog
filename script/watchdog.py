#!/usr/bin/python
# _*_ coding:utf-8 _*_

import threading
import analyzetool
import loglist

# 批量分析日志
def analyze_batch():
    serverlist = loglist.getloglist()
    port = 22
    for s in serverlist:
        th = threading.Thread(target=analyzetool.analyze, args=(s.host, s.path, s.filename, s.user, s.password, port))
        th.start()
        
analyze_batch()
