import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
sum = 0

address = input('Enter location: ')
if len(address) < 1:
    while True:
        address = input('Enter location: ')


uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
tree = ET.fromstring(data)

results = tree.findall('.//count')

for result in results:
    sum = int(result.text) + sum
    count = count + 1


print('Sum:', sum)
print('Count:', count)
