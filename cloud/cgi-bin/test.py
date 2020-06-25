#!/usr/bin/python2

import cgi
import commands
import os
import MySQLdb
import cgitb

cgitb.enable()



print 'content-type: text/html\n'
print 



data=cgi.FormContent()


con=MySQLdb.connect("localhost")
q=con.cursor()
q.execute("use mysql;")
q.execute("use login;")
p=q.execute("insert into cloud values('dibakar','dibakar@g.com','pass');")
q.execute("commit")	
	
