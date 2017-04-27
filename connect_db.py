import ibm_db
from ibm_db import connect

def connection():
	try:
#		conn = ibm_db.connect('DATABASE=IGI_DB;'
#						'HOSTNAME=10.51.227.228;'
#						'PORT=50000;'
#						'PROTOCOL=TCPIP;'
#						'UID=igiinst;'
#						'PWD=ideas;', '', '')
		conn = ibm_db.connect("dsn=jdbc:db2://10.51.227.228:50000/IGI_DB","igiinst","ideas")
	except:
		print "no connection:", ibm_db.conn_errormsg()
	else:
		print("connection successful......!!")