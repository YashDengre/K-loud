#!/usr/bin/python2

import MySQLdb
import mysql.connector as mariadb  
import cgi
import cgitb
import mariadb

cgitb.enable()

print "content-type:text/html\n"

print ""







data=cgi.FormContent()	
	
try:
	user=data['userR'][0]
	password=data['password'][0]
	email=data['email'][0]
	x=mariadb.connect(user='root',password='redhat',database='login')  
	y=x.cursor()
	sqlquery="select email from cloud where name=%s"	
	y.execute(sqlquery,(emai))
	result=y.fetchone()
	trigger=str(result)
	if(trigger=='None'):
		sqlquery="insert into cloud values(%s,%s,%s);"
		y.execute(sqlquery,(user,password,email))
		x.commit()
		print "<script>alert('Successfully Registered !')</script>"
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.112/index.html\">\n"
	else:
		print "<script>alert('Error !')</script>"
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.43.112/index.html\">\n"
except:
	print"<script>alert('error')</script>"
	






				







