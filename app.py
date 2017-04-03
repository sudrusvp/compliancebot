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
from watson_developer_cloud import ToneAnalyzerV3
import tone_detection
import cgi


conversation = ConversationV1(
    username='81cae901-ee0e-4066-b333-c6d9cc5532ec',
    password='NCdy2rD8GQ5N',
    version='2017-02-03')

conv_workspace_id = 'e5fa2b42-e839-4e1b-9c6d-4d3ca9a93330'
context={}

tone_analyzer = ToneAnalyzerV3(
    username = '20c2903e-48a9-4fd5-8f0b-5e699fa5343e',
    password = 'ZC2WBeLbXUXs',
    version = '2016-05-19')

maintainToneHistoryInContext = True 

app = Flask(__name__, static_url_path='/static')
@app.route("/", methods=['GET', 'POST'])

def main_page():

	if request.method == 'GET':
		return render_template("index2.html")	

	elif request.method == 'POST':
		
		tone = tone_analyzer.tone( text = request.form['message'])
		#conversation_payload = tone_detection.updateUserTone(payload, tone, maintainToneHistoryInContext)
		print(json.dumps(tone,indent=2))
		context = {
			"user":tone['document_tone']['tone_categories']
		}
		#print(json.dumps(context['user'][1]['category_name'],indent=4))
		response = conversation.message(workspace_id = conv_workspace_id, message_input={'text': request.form['message']},context = context)
		if response['intents'] and response['intents'][0]['confidence']:
			confidence = str(round(response['intents'][0]['confidence'] * 100))
			response = str(response['output']['text'][0] + "\n" + "<HTML><BODY><hr style='background-color: #fff;border-top: 2px dashed #8c8b8b;width:200px;margin-left:0px'></body></html>I'm "  + confidence + "% certain about this answer")
		#print(json.dumps(response,indent=2))
		return str(response)
		

if __name__ == "__main__":
	port = int(os.getenv('PORT', 5000))
	print "Starting app on port %d" % port
	app.run(debug=True, port=port, host='0.0.0.0')
	
	

