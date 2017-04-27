import ibm_db
import jaydebeapi
from ibm_db import connect

def connection():
	conn = ibm_db.connect("DRIVER={IBM DB2 JDBC Universal Driver Architecture};DATABASE=IGI_DB;HOSTNAME=10.51.227.228;PORT=50000;PROTOCOL=TCPIP;UID=igiinst;PWD=ideas;", "","")
#	conn = jaydebeapi.connect('com.ibm.db2.jcc.DB2Driver', ['jdbc:db2://10.51.227.228:50000/IGI_DB','igiinst','ideas'])
	if conn:
		print "Connection succeeded."
		ibm_db.close(conn)
	else:
		print "Connection failed."