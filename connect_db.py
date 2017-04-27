import ibm_db
from ibm_db import connect

def connection():
	try:
		conn = ibm_db.connect("DRIVER={IBM DB2 JDBC Universal Driver Architecture};DATABASE=IGI_DB;HOSTNAME=10.51.227.228;PORT=50000;PROTOCOL=TCPIP;UID=igiinst;PWD=ideas;", "","")
		print "Connection succeeded..........!!"
	except:
		print "connection unsuccessful.....!!"
	finally:
		try:
			ibm_db.close(conn)
		except:
			print "can not close conn......!!"