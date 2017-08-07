from setuptools import setup,

setup(
	name = 'geo-locater',
	version='0.01',
	packages = ['geo-locater', 'api'],
	include_package_data = True,
	install_requires = ['geoip2'],


)