import ibm_db
from ibm_db import connect

def connection():
	try:
		conn = ibm_db.connect("DRIVER={IBM DB2 JDBC DRIVER};DATABASE=IGI_DB;HOSTNAME=10.51.227.228;PORT=50000;PROTOCOL=SOCKET;UID=igiinst;PWD=ideas;AUTH_USER=admin;AUTH_PASS=admin", "","")
		print "Connection succeeded..........!!"
	except:
		print "connection unsuccessful.....!!"
		print ibm_db.conn_errormsg()
	finally:
		try:
			ibm_db.close(conn)
		except:
			print "can not close conn......!!"