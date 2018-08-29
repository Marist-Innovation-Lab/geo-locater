# geo-locator

geo-locator is an application that maps an IP address to a Location (latitude, longitude, country).

## New Features!
  - API has just been added and updated to return json formatted results.

## IP Geolocation Usage
IP geolocation is inherently imprecise. Locations are often near the center of the population. Any location provided by a GeoIP2 database or web service should not be used to identify a particular address or household.
### Tech

geo-locator uses a number of open source projects to work properly:

* [geoIP] - Provides the database reader needed to read the .mmdb binaries
* [MaxMind] - Provides the .mmdb binaries
* [flask] - a microframework for Python
* [flask-socketio] - a websocket addon for Flask
* [eventlet] - a python networking library
* [python](https://www.python.org/download/releases/2.7/) - Python 2.6 or newer is required. Not tested on Python 3.

### Installation

geo-locator requires [flask], [eventlet], [flask-socketio],and [geoIP] to work properly (all requirements should install if you follow the instructions below). To begin installation you must have Python 2.7.

##### 0.5 Navigate to the proper directory:
```sh
$ cd geo-locater
```

##### 1. Install dependencies inside the virtualenv:
```sh
$ pip install -r requirements.txt
```

##### 3. Run the server!
```sh
$ cd geo-locater
$ ./app.py
```

##### 4. Test results
Navigate to your front facing IP `http://<your-ip>:8080`



### Docker Deployment

To run an instance of the geo-locater API with docker you can either create your own image based off the Dockerfile located in the root of the directory or pull and use the image in [Docker Hub](https://hub.docker.com/r/dgisolfi/geo-locater/). If this is your first time using Docker and need to install the program, refer to the following guide otherwise you may skip to Deploying the API

#### Installing Docker

*The following is an installation guide for Docker and on a Ubuntu host machine for guides on other distros and operating systems refer to [here](https://docs.docker.com/install/)*

 First, install the latest version of Docker by running: 

```bash
sudo apt-get install Docker
```

After installation is complete, test the installation by running:

```bash
docker ps -a
```

If Docker is working properly, the output should show what containers are currently running on your host (none will be running if Docker was just installed). A common issue is not having the proper permissions to run Docker. 

 If running the above command yields a result similar to "permission denied", run the following to resolve this:

```bash
# Add Docker as a group
sudo groupadd Docker
# Add yourself to the group
sudo usermod -aG Docker <USER>
```

Docker should now be set up.

#### Deploying the API

To deploy the API run the following on the host machine. If you have built an image based of the Dockerfile use your image name at the end of the command rather than the defualt.

```bash
 docker run --rm --name geo-locater -p8080:8080 dgisolfi/geo-locater
```

After running this command the API should be accessesible from port 8080 of the host machine.

### Todos


 - Implement the free MaxMind ISP 
 - moar things

License
----
MIT
This product includes GeoLite2 data created by MaxMind, available from [MaxMind].

[maxmind]: <http://www.maxmind.com>
[geoip]: <https://github.com/maxmind/GeoIP2-python>
[flask]: <http://flask.pocoo.org/>
[virtualenv]: <https://pypi.python.org/pypi/virtualenv>
[flask-socketio]: <https://flask-socketio.readthedocs.io/en/latest/>
[eventlet]: <http://eventlet.net/>
