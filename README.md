watchdog
========

生产服务器错误日志分析工具

使用说明：
1.打开server.txt文件，配置要分析的服务器名（比如ctu.stable.alipay.net），错误日志路径（比如/home/admin/logs/ctu.stable.alipay.net），错误日志名（比如common-error.log）,登录到此服务器的用户名(比如log)和密码（比如xixihaha）,中间用英文逗号（,）分隔。
2.执行命令python watchdog.py
3.查看新生成的文件，命名为服务器名-时间-类型，比如ctu-2013-stat.txt是错误日志分析统计的结果，ctu-2013-content.txt是错误日志示例内容的结果。
