import json
import urllib
import os
import os.path
import sys
import logging
from flask import Flask
from flask import render_template
from flask import request, url_for, make_response
from dotenv import load_dotenv, find_dotenv
from watson_developer_cloud import ConversationV1
from watson_developer_cloud import ToneAnalyzerV3
import tone_detection
load_dotenv(find_dotenv())

conversation = ConversationV1(
    username='81cae901-ee0e-4066-b333-c6d9cc5532ec',
    password='NCdy2rD8GQ5N',
    version='2017-02-03')

conv_workspace_id = 'e5fa2b42-e839-4e1b-9c6d-4d3ca9a93330'
#context={

tone_analyzer = ToneAnalyzerV3(
    username = '20c2903e-48a9-4fd5-8f0b-5e699fa5343e',
    password = 'ZC2WBeLbXUXs'
    version = '2016-05-19')

maintainToneHistoryInContext = True 

app = Flask(__name__, static_url_path='/static')
@app.route("/", methods=['GET', 'POST'])

def main_page():

	if request.method == 'GET':
		return render_template("index2.html")	

	elif request.method == 'POST':
		
		payload = {
    		'workspace_id': conv_workspace_id,
 	 		'input': {
        		'text': request.form['message']
    		}
		}
		
		tone = tone_analyzer.tone(text=payload['input']['text'])
		conversation_payload = tone_detection.\
        	updateUserTone(payload, tone, maintainToneHistoryInContext)
        	
		response = conversation.message( workspace_id = conv_workspace_id,
										 message_input=conversation_payload['input'],
                                   		 context=conversation_payload['context'])
		print(json.dumps(response,indent=2))
		return str(response['output']['text'][0])
		

if __name__ == "__main__":
	port = int(os.getenv('PORT', 5000))
	print "Starting app on port %d" % port
	app.run(debug=True, port=port, host='0.0.0.0')
	
	

