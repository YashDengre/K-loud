#!/usr/bin/python2

import cgi
import commands
import os
import MySQLdb
import mysql
import cgitb
import mysql.connector as mariadb 
import random
from os import environ
cgitb.enable()


print 'content-type: text/html\n'
print "\n"




if environ.has_key('HTTP_COOKIE'):
	for cookie in map(strip,split(environ['HTTP_COOKIE'],';')):
		(key,value) = split(cookie,'=');
		if key == 'UserName':
			user=value
		if key == 'Password':
			passwd=value

"""
print "<pre style='color:red; font-size:30px;'>"
print "user = {}".format(user)
print "</pre>"
"""
data=cgi.FormContent()



con=MySQLdb.connect("localhost",'root','redhat')
q=con.cursor()
image=data['image'][0]
ram  = data['ram'][0]
hdd  = data['hdd'][0]
cpu  = data['cpu'][0]
port=str(random.randint(5556,5899))
rport=str(random.randint(5900,5999)) 

q.execute("use mysql;")
q.execute("use login;")
p=q.execute("insert into clouduse values('{}','{}','{}','{}')".format('demo',rport,image,port))
q.execute("commit")

if image=="redhat":
	commands.getstatusoutput("sudo ln /var/lib/libvirt/images/redhat.qcow2     /root/Desktop/iaas/demo.qcow2")
elif image=="windows":
	commands.getstatusoutput("sudo ln /var/lib/libvirt/images/windows.qcow2     /root/Desktop/iaas/demo.qcow2")
elif image=="kali":
	commands.getstatusoutput("sudo ln /root/Desktop/iaas/kali.qcow2     /root/Desktop/iaas/{}.qcow2")
else:
	commands.getstatusoutput("sudo ln /root/Desktop/iaas/mint.qcow2     /root/Desktop/iaas/{}.qcow2")		


result=commands.getstatusoutput("sudo virt-install --import  --name demo  --memory {}   --vcpu {}  --disk path=/root/Desktop/iaas/demo.qcow2 --noautoconsole  --graphics vnc,listen=0.0.0.0,port={}".format(ram,cpu,rport))



if result[0]==0:
	commands.getstatusoutput("sudo /var/www/cgi-bin/websockify-master/run -D 192.168.43.202:{} 192.168.43.202:{}".format(port,rport))
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.202/noVNC-master/vnc_auto.html?host=192.168.43.202&port={}\">\n".format(port)
else:
	print "<script> alert('Error! {}')</script>".format(result[1])
	

