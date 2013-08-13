#!/usr/bin/python
# _*_ coding:utf-8 _*_

# 此类定义一个错误的完整信息

class KEYFACTOR:
    # 错误关键字
    key_word = None
    # 错误的详细内容
    key_content = ''
    # 错误的出现次数  
    key_count = 0
    # 错误的首次出现时间
    first_time = None
    # 错误的最后出现时间
    last_time = None
    # 出错时间列表，用于按小时按分钟统计
    time_list = []
     
    def _init_(self, word, content):
        self.key_word = word
        self.key_content = content
        self.key_count = 0
