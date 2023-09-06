import json
import urllib.request, urllib.parse, urllib.error

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

address = 'https://py4e-data.dr-chuck.net/json'
while True:
    address = input('Enter Location - ')
    if len(address) > 1: break


parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url)
# print(type(uh))
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

# print(type(data))
info = json.loads(data)
# print(type(info))



print(info)

print('Place Id:', info['results'][0]['place_id'])




