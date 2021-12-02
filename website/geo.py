import geopy.distance
import requests

coords_1 = (31.511071, 74.351114)
coords_2 = (31.508137, 74.350459)

print ("Distance: ",geopy.distance.geodesic(coords_1, coords_2).km)

import mpu

# Point one
lat1 = 31.511071
lon1 = 74.351114

# Point two
lat2 = 31.508137
lon2 = 74.350459

# What you were looking for
dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
print(dist)

coords_1 = (31.511071, 74.351114)
coords_2 = (31.508137, 74.350459)
dist = mpu.haversine_distance(coords_1, coords_2)
print(dist)


url = 'https://nominatim.openstreetmap.org/search'
addr = '72 MB Floor Zainab tower, Link road, Model town, Lahore, Pakistan'
headers = {'User-Agent': 'Odoo (http://www.odoo.com/contactus)'}
response = requests.get(url, headers=headers, params={'format': 'json', 'q': addr})
print(response.json())
print('openstreetmap nominatim service called')

#import requests
#import urllib.parse

#address = 'Shivaji Nagar, Bangalore, KA 560001'
#url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

#response = requests.get(url).json()
#print(response[0]["lat"])
#print(response[0]["lon"])
