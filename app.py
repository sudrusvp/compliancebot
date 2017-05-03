import json
import urllib
import os
import os.path
import sys
import datetime
import connect_db as db
from flask import Flask
from flask import render_template
from flask import request, url_for, make_response
from watson_developer_cloud import ConversationV1
from os.path import join, dirname



conversation = ConversationV1(
    username='8b39e53f-697e-4c3a-aee7-efc78061bce0',
    password='SehjL5SoP2wl',
    version='2017-02-03')

conv_workspace_id = '63426865-ec68-48db-a233-3d58e03ffe67'
app = Flask(__name__, static_url_path='/static')
fullpath = "xyz"
context = {}

@app.route("/", methods=['GET', 'POST'])
def main_page():
	
	if request.method == 'GET':
		global fullpath
		global context
		filename = 'static/doc/myfile-%s.txt'%datetime.datetime.now().strftime('%Y%m%d-%H%M&S')
		print filename
		fullpath = filename
		print fullpath
		context_file = open(fullpath,'w+')
		context_file.write(context)
		context_file.close()
				
		return render_template("index2.html")
		
	elif request.method == 'POST':
		global fullpath
		global context
		file = open(fullpath,'r')
		context = json.loads(file.read())
		file.close()
		
		response = conversation.message(workspace_id = conv_workspace_id, message_input={'text': request.form['message']},context = context)
		print(json.dumps(response,indent=2))
		
		file = open(fullpath,'w')
		print("Writing " + str(json.dumps(response['context'])) + "to file........")
		file.write(str(json.dumps(response['context'])))
		file.close()
		
		script1 = """<html><head><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>
			<script type="text/javascript">
			/*eslint-env jquery */
			function yes() {
				alert("Thank you!");
			}
			function no() {
				alert("Thank you!");
			}
			</script>
			</head>
			<body>
			<hr>
			<a href='#' class='btn btn-info btn-lg' onclick='yes()'>
          	<span class='glyphicon glyphicon-thumbs-up'></span> Yes
        	</a>
			<a href='#' class='btn btn-info btn-lg' onclick='no()'>
          	<span class='glyphicon glyphicon-thumbs-down'></span> No
    		</a>
			</body>
			</html>"""
		response = str(response['output']['text'][0]) + script1
		return str(response)
		

if __name__ == "__main__":
	port = int(os.getenv('PORT', 5000))
	print "Starting app on port %d" % port
	app.run(debug=True, port=port, host='0.0.0.0')
	
	

