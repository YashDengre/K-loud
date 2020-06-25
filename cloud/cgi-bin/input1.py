#!/usr/bin/python2

import cgi
import commands
import os
print 'content-type: text/html\n'
print 


data=cgi.FormContent()

cmd=data['n1'][0]
#cmd2=data['n2'][0]
#commands.getstatusoutput("sudo export DISPLAY=:0.0")
#commands.getstatusoutpit("echo $DISPLAY")
out=commands.getstatusoutput("sudo  useradd {}".format(cmd))
#out=commands.getstatusoutput("sudo sshpass -p yash ssh  -X yashdengre@192.168.43.202  {} ".format(cmd))


print """ <style> pre {color:red;}</style>"""
print"<pre>" 
print out[1]
print"</pre>"

#cip=os.environ("REMOTE_ADDR") #for cookies or session purpose
#print cip[0]
#print "hello"
#data= cgi.FormContent()
#print data.['x'][0]t
