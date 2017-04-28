import ibm_db
import MySQLdb
from ibm_db import connect

def connection():
#	try:
#		conn = ibm_db.connect("DRIVER={IBM DB2 JDBC DRIVER};DATABASE=IGI_DB;HOSTNAME=10.51.227.228;PORT=50000;PROTOCOL=TCPIP;UID=igiinst;PWD=ideas;","","")
#		conn = ibm_db.connect("dsn=jdbc:db2://10.51.227.228:50000/IGI_DB;PROTOCOL=TCPIP;UID=igiinst;PWD=ideas;", "","")
	conn = MySQLdb.connect("localhost","root","admin","test" )
#		conn=MySQLdb.connect(host=####, user=####, passwd=####, db=####)
		
#		print "Connection succeeded..........!!"
#	except:
#		print "connection unsuccessful.....!!"
##		print ibm_db.conn_errormsg()
#	finally:
#		try:
#			conn.close()
#		except:
#			print "can not close conn......!!"