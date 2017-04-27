import ibm_db
from ibm_db import connect

def connection():
	try:
#		conn = ibm_db.connect("DRIVER={IBM DB2 JDBC DRIVER};DATABASE=IGI PSL 5.2.2;HOSTNAME=10.51.227.228;PORT=50000;PROTOCOL=TCPIP;UID=igiinst;PWD=ideas;", "admin","admin")
		conn = ibm_db.connect("jdbc:db2://10.51.227.228:50000/IGI_DB;PROTOCOL=TCP/IP;UID=igiinst;PWD=ideas;", "","")
		print "Connection succeeded..........!!"
	except:
		print "connection unsuccessful.....!!"
		print ibm_db.conn_errormsg()
	finally:
		try:
			ibm_db.close(conn)
		except:
			print "can not close conn......!!"