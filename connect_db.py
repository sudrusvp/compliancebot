import ibm_db
from ibm_db import connect

def connection():
	try:
		conn = ibm_db.connect('DATABASE=IGI_DB;'
						'HOSTNAME=10.51.227.228;'
						'PORT=50000;'
						'PROTOCOL=TCPIP;'
						'UID=igiinst;'
						'PWD=ideas;', '', '')
	except:
		print "DB connection error......!!"
	else:
		print("connection successful......!!")