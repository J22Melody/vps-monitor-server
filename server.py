
import Pyro4
import re,urllib2
from monitor import *

# get ip

class Getmyip:
    def getip(self):
        try:
            myip = self.visit("http://www.ip138.com/ip2city.asp")
        except:
            try:
                myip = self.visit("http://www.bliao.com/ip.phtml")
            except:
                try:
                    myip = self.visit("http://www.whereismyip.com/")
                except:
                    myip = "So sorry!!!"
        return myip
    def visit(self,url):
        opener = urllib2.urlopen(url)
        if url == opener.geturl():
            str = opener.read()
        return re.search('\d+\.\d+\.\d+\.\d+',str).group(0)
getmyip = Getmyip()
localip = getmyip.getip()

# vps-monitor service

vps_monitor=Monitor()

# launch service

Pyro4.config.HOST = localip
Pyro4.config.HMAC_KEY = '123456'

daemon=Pyro4.Daemon(port=7555)                 # make a Pyro daemon
uri=daemon.register(vps_monitor, "monitor")   

print "Object uri =", uri 

daemon.requestLoop()                  # start the event loop of the server to wait for calls


