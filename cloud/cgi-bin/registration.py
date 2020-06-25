#!/usr/bin/python2


#mconnecting through mysqldb

import cgi
import commands
import os
import MySQLdb
import mysql
import cgitb
import mysql.connector as mariadb 
cgitb.enable()



print 'content-type: text/html\n'
print 



data=cgi.FormContent()
#con=mariadb.connect(user='',password='',database='login')

con=MySQLdb.connect("localhost",'root','redhat')
q=con.cursor()
value1=data['userR'][0]
value2=data['password'][0]
value3=data['email'][0]	
q.execute("use mysql;")
q.execute("use login;")
p=q.execute("insert into cloud values('{}','{}','{}')".format(value1,value3,value2))
q.execute("commit")
o=commands.getstatusoutput("sudo useradd {}".format(value1))
r=commands.getstatusoutput("sudo echo {} | spasswd {}".format(value2,value1))
if p == 1:
		print "<script> alert('Registration Successfull You Can Login now!')</script>"
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.202/index.html\">\n"
else :
		print "<script> alert('Error!')</script>"
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.202/index.html\">\n"
		
		

