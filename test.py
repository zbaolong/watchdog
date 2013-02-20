import server
import analyzetool 
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
analyzetool.analyze()
