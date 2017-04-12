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
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1


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

#maintainToneHistoryInContext = True 

text_to_speech = TextToSpeechV1(
    username='8921eb13-5eb4-4286-9add-5a7870ba4ecf',
    password='tKJBMhuw42nL',
    x_watson_learning_opt_out=True)


app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET', 'POST'])
def main_page():

	if request.method == 'GET':
		return render_template("index2.html")

	elif request.method == 'POST':
		
		tone = tone_analyzer.tone( text = request.form['message'])
		#conversation_payload = tone_detection.updateUserTone(payload, tone, maintainToneHistoryInContext)
		#print(json.dumps(tone,indent=2))
		context = {
			"user":tone['document_tone']['tone_categories']
		}
		#print(json.dumps(context['user'][1]['category_name'],indent=4))
		response = conversation.message(workspace_id = conv_workspace_id, message_input={'text': request.form['message']},context = context)
#		with open(join(dirname(__file__), 'audio/output.wav'),'wb') as audio_file:
#    		audio_file.write(text_to_speech.synthesize(str(response['output']['text'][0]) , accept='audio/wav',voice="en-US_AllisonVoice"))
#		print(
#    		json.dumps(text_to_speech.pronunciation(
#        		'Watson', pronunciation_format='spr'), indent=2))

		#print(json.dumps(text_to_speech.customizations(), indent=2))
		#print(json.dumps(response,indent=2))
#		a = str(context['user'][0]['category_name']) + "--->" + str(context['user'][0]['tones'][0]['tone_name']) + "-" + str(round(context['user'][0]['tones'][0]['score'],2))
#		b = str(context['user'][0]['tones'][1]['tone_name']) + "-" + str(round(context['user'][0]['tones'][1]['score'],2))
#		c = str(context['user'][0]['tones'][2]['tone_name']) + "-" + str(round(context['user'][0]['tones'][2]['score'],2))
#		d = str(context['user'][0]['tones'][3]['tone_name']) + "-" + str(round(context['user'][0]['tones'][3]['score'],2))
#		e = str(context['user'][0]['tones'][4]['tone_name']) + "-" + str(round(context['user'][0]['tones'][4]['score'],2))
#		
#		f = str(context['user'][1]['category_name']) + "--->" +str(context['user'][1]['tones'][0]['tone_name']) + "-" + str(round(context['user'][1]['tones'][0]['score'],2))
#		g = str(context['user'][1]['tones'][1]['tone_name']) + "-" + str(round(context['user'][1]['tones'][1]['score'],2))
#		h = str(context['user'][1]['tones'][2]['tone_name']) + "-" + str(round(context['user'][1]['tones'][2]['score'],2))
#		
#		i = str(context['user'][2]['category_name']) + "--->" +str(context['user'][2]['tones'][0]['tone_name']) + "-" + str(round(context['user'][2]['tones'][0]['score'],2))
#		j = str(context['user'][2]['tones'][1]['tone_name']) + "-" + str(round(context['user'][2]['tones'][1]['score'],2))
#		k = str(context['user'][2]['tones'][2]['tone_name']) + "-" + str(round(context['user'][2]['tones'][2]['score'],2))
#		l = str(context['user'][2]['tones'][3]['tone_name']) + "-" + str(round(context['user'][2]['tones'][3]['score'],2))
#		m = str(context['user'][2]['tones'][4]['tone_name']) + "-" + str(round(context['user'][2]['tones'][4]['score'],2))
		
#		#for emotion tone
#		i = 0
#		j = 0
#		max = 0.0
#		while i != 5:
#			temp = round(context['user'][0]['tones'][i]['score'],2)
#			if temp >= max:
#				max = temp
#				j = i
#			i+=1
#		
#		final_emotiontone = str(context['user'][0]['tones'][j]['tone_name']) + "-" + str(round(context['user'][0]['tones'][j]['score'],2))
#		
#		#for language tone
#		i = 0
#		j = 0
#		max = 0.0
#		while i != 3:
#			temp = round(context['user'][1]['tones'][i]['score'],2)
#			if temp >= max:
#				max = temp
#				j = i
#			i+=1
#		
#		final_langtone = str(context['user'][1]['tones'][j]['tone_name']) + "-" + str(round(context['user'][1]['tones'][j]['score'],2))
#		
#		#for social tone
#		i = 0
#		j = 0
#		max = 0.0
#		while i != 5:
#			temp = round(context['user'][2]['tones'][i]['score'],2)
#			if temp >= max:
#				max = temp
#				j = i
#			i+=1
#		
#		final_socialtone = str(context['user'][2]['tones'][j]['tone_name']) + "-" + str(round(context['user'][2]['tones'][j]['score'],2))
		
		if response['intents'] and response['intents'][0]['confidence']:
			confidence = str(round(response['intents'][0]['confidence'] * 100))
			response = str(response['output']['text'][0] + "\n" + "<HTML><BODY><hr style='height: 7px;border: 0;box-shadow: 0 10px 10px -10px white inset;width:270px;margin-left:0px'></body></html>I'm "  + confidence + "% certain about this answer!")
			newline = "<html><body><br></body></html>"
#			response = response + newline + a + " " + b + " "+ c + " "+ d + " "+ e 
#			response = response + newline + f + " " + g + " "+ h
#			response = response + newline + i + " " + j + " "+ k + " "+ l + " "+ m
#			response = response + newline + " detected " + final_emotiontone + newline + " detected " + final_langtone + newline + " detected " + final_socialtone
			response = response + newline + "<html><body><hr></body></html>"
			script = """<html><head><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>
			</head>
			<body>
			<a href='#' class='btn btn-info btn-lg' onclick='yes()'>
          	<span class='glyphicon glyphicon-thumbs-up'></span> Yes
        	</a>
			<a href='#' class='btn btn-info btn-lg' onclick='no()'>
          	<span class='glyphicon glyphicon-thumbs-down'></span> No
        	</a>
			</body>
			</html>"""
			
			response = response + script
			return str(response)
			
		#else
			#return str(response)
			
		print(json.dumps(response,indent=2))
		return str(response['output']['text'][0])
		

if __name__ == "__main__":
	port = int(os.getenv('PORT', 5000))
	print "Starting app on port %d" % port
	app.run(debug=True, port=port, host='0.0.0.0')
	
	

