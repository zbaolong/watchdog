import sys
sys.path.append("../script/")
import server
import analyzetool 
import errorinfo
def servertest():
 serverlist = server.getserverlist()
 for s in serverlist:
  host = s.host
  print host
def testanalyze():
 host = 'ctu.stable.alipay.net'
 path = '/home/admin/logs/ctu.stable.alipay.net'
 filename = 'common-error.log'
 username = 'admin'
 password = 'alipaystable'
 analyzetool.analyzeSignal(host,path,filename,username,password)
def testerrorinfo():
 host = 'gege'
 keylist = 'key'
 content = 'conte'
 errorinfo.recordError(host,keylist,content) 
testerrorinfo()
