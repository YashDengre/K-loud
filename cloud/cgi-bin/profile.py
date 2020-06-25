#!/usr/bin/python2

import cgi
import commands
import os


print 'content-type: text/html\n'
print 


data=cgi.FormContent()



cmd=data['soft'][0]
#commands.getstatusoutput("sudo export DISPLAY=:1")
f=open('/root/Desktop/saas.txt','w')
f.write("ssh -X yashdengre@192.168.43.202  {}".format(cmd))
f.close()
commands.getstatusoutput("scp /root/Desktop/saas.txt   root@192.168.43.240:/root/Desktop/")
out=commands.getstatusoutput("sudo sshpass -p yash ssh  -X yashdengre@192.168.43.202  {}   ".format(cmd))
print"<pre>" 
print out[1]
print"</pre>"




#iaas service 

image=data['image'][0]
ram  = data['ram'][0]
hdd  = data['hdd'][0]
cpu  = data['cpu'][0]
if image=="redhat":
	commands.getstatusoutput("sudo cp /root/Desktop/iaas/redhat.qcow2     /root/Desktop/iaas/{}.qcow2".format(user))
elif image="windows":
	commands.getstatusoutput("sudo cp /root/Desktop/iaas/cloud1.qcow2     /root/Desktop/iaas/{}.qcow2".format(user))
elif image="kali":
	commands.getstatusoutput("sudo cp /root/Desktop/iaas/kali.qcow2     /root/Desktop/iaas/{}.qcow2".format(user))
else:
	commands.getstatusoutput("sudo cp /root/Desktop/iaas/mint.qcow2     /root/Desktop/iaas/{}.qcow2".forma(user))		



commands.getstatusoutput("sudo virt-install --import  --name {}  --memory {}   --vcpu {} --vnc --vncport={} --vnclisten=0.0.0.0  --disk path= /root/Desktop/iaas/{}.qcow2".format(user,ram,cpu,portno)


#cip=os.environ("REMOTE_ADDR") #for cookies or session purpose
#print "<pre>"i
#print cip[0]
#print "</pr


