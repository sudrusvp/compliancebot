import ibm_db
import MySQLdb
from ibm_db import connect

def connection():
	try:
#		conn = ibm_db.connect("DRIVER={IBM DB2 JDBC DRIVER};DATABASE=IGI_DB;HOSTNAME=10.51.227.228;PORT=50000;PROTOCOL=TCPIP;UID=igiinst;PWD=ideas;","","")
#		conn = ibm_db.connect("dsn=jdbc:db2://10.51.227.228:50000/IGI_DB;PROTOCOL=TCPIP;UID=igiinst;PWD=ideas;", "","")
		conn = MySQLdb.Connection(host='127.0.0.1', port=3306,user='root', passwd='admin', db='test')
		
		print "Connection succeeded..........!!"
	except Exception as e:
		print e
#		print ibm_db.conn_errormsg()
	finally:
		try:
			conn.close()
		except:
			print "can not close conn......!!"