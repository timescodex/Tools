#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib, urllib2
import json
import sys
import re
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer


#create a webservice to offer the ip-address via taobao:
#def getLocationFromIP(ip):
ip = raw_input(r'IP : ')
ip = str.strip(ip)
ptn = re.compile(r'(([12][0-9][0-9]|[1-9][0-9]|[1-9])\.){3,3}([12][0-9][0-9]|[1-9][0-9]|[1-9])')
rel = ptn.match(ip)

if rel:
    pass
else:
    print "IP  wrong"
    sys.exit()

try:
    urlfp = urllib.urlopen('http://ip.taobao.com/service/getIpInfo.php?ip=' + ip)
except Exception, e:
    print "Error ", e
    sys.exit()

ipdata = urlfp.read()
urlfp.close()

allinfo = json.loads(ipdata)

for oneinfo in allinfo:
    if "code" == oneinfo:
        if 0 == allinfo[oneinfo]:
            print "ip   : " + allinfo["data"]["ip"]
            print "city : " + allinfo["data"]["country"],
            print allinfo["data"]["region"],
            print allinfo["data"]["city"],
            print "(" + allinfo["data"]["isp"] + ")"
            
        else:
            print "parse error"
            sys.exit()




