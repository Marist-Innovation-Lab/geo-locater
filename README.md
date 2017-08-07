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
* [python](https://www.python.org/download/releases/2.7/) - Python 2.6 or newer is required. Not tested on Python 3.
* [virtualenv] - a highly reccomended python virtual environment builder [read more](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)

### Installation

geo-locator requires [flask], [virtualenv], and [geoIP] to work properly (all requirements should install if you follow the instructions below). To begin installation you must have Python 2.7.


#### 0.5 Install virtualenv
'''sh
$ pip install virtualenv
'''

##### 1. Create and initialize flask virtualenv for the project:


```sh
$ cd geo-locater
$ virtualenv flask
New python executable in flask/bin/python
Installing setuptools............................done.
Installing pip...................done.
$ flask/bin/pip install flask
```

##### 2. Setup and install dependencies


```sh
$ python setup.py install
```

##### 3. Run the server!
```sh
$ cd geo-locater
$ python app.py
```

##### 4. Test results
Navigate to your front facing IP `http://<your-ip>:8080`

### Todos


 - Implement the free MaxMind ISP 
 - moar things

License
----
This product includes GeoLite2 data created by MaxMind, available from [MaxMind].

   [maxmind]: <http://www.maxmind.com>
   [geoip]: <https://github.com/maxmind/GeoIP2-python>
   [flask]: <http://flask.pocoo.org/>
   [virtualenv]: <https://pypi.python.org/pypi/virtualenv>
