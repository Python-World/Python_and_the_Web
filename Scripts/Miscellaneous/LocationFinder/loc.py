import requests
import json

baseurl = "http://py4e-data.dr-chuck.net/json"

i = 0
loc, place = [], []
while i != 2:
	i += 1
	address = input("Enter address: ")
	if len(address) < 1: break

	params = {}
	params['address'] = address
	params['key'] = 42
	req = requests.get(baseurl, params = params)
	
	data = req.text
	try:
		js = json.loads(data)
	except :
		js = None

	if not js or 'status' not in js or js['status'] != 'OK':
		print("failed to load data!!!")
		continue

	lat = js['results'][0]['geometry']['location']['lat']
	lng = js['results'][0]['geometry']['location']['lng']
	location = js['results'][0]['formatted_address']
	print("Location: ",location)
	loc.append([lat,lng])
	place.append(location)
	print("lat {}, lng {}".format(lat,lng))
