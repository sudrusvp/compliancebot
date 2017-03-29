import json
import urllib
import os
import os.path
import sys
import logging
from flask import Flask
from flask import render_template
from flask import request, url_for, make_response
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
    username='81cae901-ee0e-4066-b333-c6d9cc5532ec',
    password='NCdy2rD8GQ5N',
    version='2017-02-03')

workspace_id = 'e5fa2b42-e839-4e1b-9c6d-4d3ca9a93330'
context={}
app = Flask(__name__, static_url_path='/static')
@app.route("/", methods=['GET', 'POST'])

def main_page():

	if request.method == 'GET':
		return render_template("index2.html")	

	elif request.method == 'POST':
		#print("inside post1")
		#response = conversation.message(workspace_id=workspace_id, message_input={'text': request.form['message']},context=context)
		#print(response)
		#print("inside post2")
		#context = str(response['context']['context_name'])
		response = conversation.message(workspace_id=workspace_id, message_input={'text': request.form['message']},context=context)
		print(json.dumps(response, indent=2))
		#print("***********")
		print(json.dumps(response['context'], indent=2))
		#response_message = response.read();
		#response_message = json.dumps(response, indent=2)
		#res = json.load(response_message)
		#print(type(response))
		#print(str(response['output']['text'][0]))
		return str(response['output']['text'][0])
		

if __name__ == "__main__":
	port = int(os.getenv('PORT', 5000))
	print "Starting app on port %d" % port
	app.run(debug=True, port=port, host='0.0.0.0')
	
	

