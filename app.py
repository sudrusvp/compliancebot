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
from uuid import getnode as get_mac




conversation = ConversationV1(
    username='8b39e53f-697e-4c3a-aee7-efc78061bce0',
    password='SehjL5SoP2wl',
    version='2017-02-03')
print "inside global app"
conv_workspace_id = '63426865-ec68-48db-a233-3d58e03ffe67'

app = Flask(__name__, static_url_path='/static')


@app.route("/", methods=['GET', 'POST'])
def main_page():
	print "inside main"
	if request.method == 'GET':
		return render_template("index2.html")

	elif request.method == 'POST':
		data = str(request.POST.get("message",None))
		context = {}
		if os.path.getsize('static/doc/file.txt') > 0:
			file = open('static/doc/file.txt','r')
			context = json.loads(file.read())
			file.close()
		else:
			print('file is empty')
		
		response = conversation.message(workspace_id = conv_workspace_id, message_input={'text' : data },context = context)
		print("***********"+json.dumps(response,indent=2)+"***************")
			
		
		file = open('static/doc/file.txt','w+')
#		print("Writing " + str(json.dumps(response['context'])) + "to file........")
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
#		script2 = """<html>
#			<p style='visibility:hidden;' id='context' name='context'>{code}</p>
#			</html>""".format(code=str(json.dumps(response['context'])))
		response = str(response['output']['text'][0]) + script1
		print "leaving post method"
		return str(response)
		

if __name__ == "__main__":
	port = int(os.getenv('PORT', 5000))
	print "Starting app on port %d" % port
	app.run(debug=True, port=port, host='0.0.0.0')
	
	

