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


con=MySQLdb.connect("localhost",'root','redhat')
q=con.cursor()
value1=data['email'][0]
value2=data['password'][0]
q.execute("use mysql;")
q.execute("use login;")
q.fetchone()
o=q.execute("select * from cloud where email='{}' and password='{}';".format(value1,value2))
if o == 1:	
		print "Set-Cookie:UserName={};\r\n".format(value1)
		print "Set-Cookie:Password={};\r\n".format(value2)
		print "Set-Cookie:Domain=jufyo.com;\r\n"
		print "Set-Cookie:Path=/python2;\n"
		print "Content-type:text/html\r\n\r\n"
	
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.202/userprofile.html\">\n"
else:
		print "<script> alert('Password invalid')</script>"
		
		
	
