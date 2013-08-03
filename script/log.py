#!/usr/bin/python
# _*_ coding:utf-8 _*_

# 此类定义一个日志的详细信息
class LOG:
    # 主机地址
    host = None
    # 端口号
    port = 22
    # 用户名
    user = None
    # 密码
    password = None
    # 待分析日志存放目录
    path = None
    # 待分析日志名
    filename = None
    
    def _init_(self):pass
