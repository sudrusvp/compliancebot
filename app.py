import json
import urllib
import os
import os.path
import sys
import logging
import ibm_db
import connect_db
from flask import Flask
from flask import render_template
from flask import request, url_for, make_response
from watson_developer_cloud import ConversationV1
from os.path import join, dirname
from connect_db import connection


conversation = ConversationV1(
    username='8b39e53f-697e-4c3a-aee7-efc78061bce0',
    password='SehjL5SoP2wl',
    version='2017-02-03')

conv_workspace_id = '63426865-ec68-48db-a233-3d58e03ffe67'
app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET', 'POST'])
def main_page():

	if request.method == 'GET':
		return render_template("index2.html")

	elif request.method == 'POST':
		context = {}
		if os.path.getsize('static/doc/file.txt') > 0:
			file = open('static/doc/file.txt','r')
			context = json.loads(file.read())
			file.close()
		else:
			print('file is empty')
			
		response = conversation.message(workspace_id = conv_workspace_id, message_input={'text': request.form['message']},context = context)
		print(json.dumps(response,indent=2))
		
		file = open('static/doc/file.txt','w')
		print("Writing " + str(json.dumps(response['context'])) + "to file........")
		file.write(str(json.dumps(response['context'])))
		file.close()

#		if response['intents'] and response['intents'][0]['confidence']:
#			confidence = str(round(response['intents'][0]['confidence'] * 100))
#			response = str(response['output']['text'][0] + "\n" + "<HTML><BODY><hr style='height: 7px;border: 0;box-shadow: 0 10px 10px -10px white inset;width:270px;margin-left:0px'></body></html>I'm "  + confidence + "% certain about this answer!")
#			return str(response)
			
		return str(response['output']['text'][0])
		

if __name__ == "__main__":
	port = int(os.getenv('PORT', 5000))
	print "Starting app on port %d" % port
	app.run(debug=True, port=port, host='0.0.0.0')
	
	

