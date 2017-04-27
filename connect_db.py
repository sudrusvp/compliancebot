import ibm_db
from ibm_db import connect

def connection():
	conn_str = "DRIVER={IBM DB2 JDBC};DATABASE=IGI_DB.IGACORE;HOSTNAME=10.51.227.228;PORT=50000;PROTOCOL=TCPIP;UID=igiinst;PWD=ideas;"
	conn = ibm_db.connect(conn_str, '', '')
	if conn:
		print "Connection succeeded."
		ibm_db.close(conn)
	else:
		print "Connection failed."