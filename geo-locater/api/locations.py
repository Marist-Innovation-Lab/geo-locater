from flask import jsonify
from app import app
from locate import findloc
import time

#define routes and methods used to navigate to said routes
@app.route('/location/<srcip_address>-<destip_address>/', methods=['GET'])
def triangulate(srcip_address,destip_address):
	srcresult  = findloc(srcip_address)
	destresult = findloc(destip_address)
	return jsonify({'source ip': srcresult, 'dest ip': destresult})

@app.route('/location/<srcip_address>/', methods=['GET'])
def geolocate(srcip_address):
	result = findloc(srcip_address)
	return jsonify(result)

@app.route('/ver/', methods=['GET'])
def printver():
	return """geo-locator ver 0.01"""

@app.route('/', methods=['GET'])
def printhelp():
	return """<h1>Welcome to the geo-locator!</h1>
	       <p> HTTP verbs used: GET [action]<br>
	       GET /ver     									- API version<br>
	       GET /date  										- current date<br>
	       GET /time										- current time<br>
	       GET /datetime 								  	- current date<br>
	       GET /location/&lt;ip address&gt;  					- get country, longitute, and latitute of ip address<br>
	       GET /location/&lt;source ip&gt;-&lt;dest ip&gt; 			- get country, longitude, and latitute of both source and destination IPs, organized</p>"""

#incase someone goes where we have nothing to show
@app.errorhandler(404)
def page_not_found(e):
	return """<h1> 404 not found buddy. . . you can try again but next time do better.</h1>"""