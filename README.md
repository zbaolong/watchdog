watchdog
========

服务器错误日志分析工具

代码目录说明：
conf  配置文件目录
result 存放所有的分析结果文件
script 存放所有的正式运行的脚本文件
tests 存放测试脚本文件
README.md 帮助文档
LICENSE.txt GNU 文件说明

环境说明：
代码开发环境为MAC 10.8 ，PYTHON 2.7.2，需要安装第三方包paramiko。

使用说明：
1.打开conf/server.txt文件，配置要分析的服务器名（比如ctu.stable.alipay.net），错误日志路径（比如/home/admin/logs/ctu.stable.alipay.net），错误日志名（比如common-error.log）,登录到此服务器的用户名(比如log)和密码（比如xixihaha）,中间用英文逗号（,）分隔。 注意：可以配置多个文件同时分析，最后一定要以,结尾。
示例:
securityprodmng.577.alipay.net,/home/admin/logs/securityprodmng.577.alipay.net,common-error.log,admin,ctutest250,
securitydata.t598.alipay.net,/home/admin/logs/securitydata,common-error.log,admin,ctu,
2.在script目录下执行命令python watchdog.py
3.查看result目录下新生成的文件，命名为服务器名-时间-类型，比如*index.txt是错误日志分析概要结果，*detail.txt是错误日志示例内容详细结果，*time.txt是错误日志时间记录，方便后续统计信息。
