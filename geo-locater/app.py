#!/usr/bin/env python
from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from locate import findloc
import json, eventlet
app = Flask(__name__)
socketio = SocketIO(app)

demo_on = 0;

#define routes and methods used to navigate to said routes
@app.route('/location/<srcip_address>-<destip_address>/', methods=['GET'])
def triangulate(srcip_address,destip_address):
	srcresult  = findloc(srcip_address)
	destresult = findloc(destip_address)
	socketio.emit('send-to-map', {'source-ip': srcresult, 'dest-ip': destresult})
	return jsonify({'source-ip': srcresult, 'dest-ip': destresult})

@app.route('/location/<srcip_address>/', methods=['GET'])
def geolocate(srcip_address):
	result = findloc(srcip_address)
	return jsonify(result)

@app.route('/ver/', methods=['GET'])
def printver():
	return """geo-locator ver 0.01"""

@app.route('/datetime/', methods=['GET'])
def printdatetime():
	return str(datetime.now())

@socketio.on('run_demo')
def run_demo():
	print("Demo Starting....")
	demo_on = 1
# read the json file 
	with open("demo/ProdDemoFileAWSandAlbanySSHHP.json") as jsonfile:
		data = json.load(jsonfile)
		for i in range(1, 55):                                     #len(data)):
			#read the data and assign variables
			srcip_address = findloc(data[i]["SrcIP"])
			destip_address = findloc(data[i]["DestIP"])
			Timestamp = float(data[i-1]["Timestamp"])
			FutureTS = float(data[i]["Timestamp"])
			wait = FutureTS - Timestamp + .500
			emit('send-to-map-withUserInfo', {'source-ip': srcip_address, 'dest-ip': destip_address, 'USERINFO' : {'username' : data[i]["User"], 'password' : data[i]["Pass"]}})
			eventlet.sleep(wait)


@app.route('/', methods=['GET'])
def printhelp():
	return """<h1>Welcome to the geo-locator!</h1>
	       <p> HTTP verbs used: GET [action]<br>
	       GET /ver     									- API version<br>
	       GET /datetime 								  	- current date<br>
	       GET /location/&lt;ip address&gt;  					- get country, longitute, and latitute of ip address<br>
	       GET /location/&lt;source ip&gt;-&lt;dest ip&gt; 			- get country, longitude, and latitute of both source and destination IPs, organized</p>"""

#incase someone goes where we have nothing to show
@app.errorhandler(404)
def page_not_found(e):
	return """<h1> 404 not found buddy. . . you can try again but next time do better.</h1>"""

if __name__ == '__main__':
	socketio.run(app,host='0.0.0.0',port='8080')
