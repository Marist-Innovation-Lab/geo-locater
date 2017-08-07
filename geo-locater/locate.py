import csv
import geoip2.database

city_mmdbdir = "./dbs/GeoLite2-City.mmdb"
isp_mmdbdir  = "./dbs/GeoIP2-ISP.mmdb"

def findloc(ip_address):
	try:
		print("Attempting to find location for: " + ip_address + "in the MaxMindDB. . .")
		reader    = geoip2.database.Reader(city_mmdbdir)
		response  = reader.city(ip_address)
		country   = response.country.name
		latitude  = response.location.latitude
		longitude = response.location.longitude
		reader.close()
		printocsv(ip_address, latitude, longitude, country)
		
		return { 
		'ip_address' : ip_address,
		'latitude'   : latitude, 
		'longitude'  : longitude, 
		'country'    : country
		}
	except:
		print("whoops that didn't work")
		return { 
		'ip address' : 0,
		'latitude'   : 0, 
		'longitude'  : 0, 
		'country'    : 0
		}
def printocsv(ip_address, latitude, longitude, country):
	with open('loc.csv', 'a') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([ip_address, latitude, longitude, country])
		csvfile.close()
