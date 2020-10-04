import urllib.request, urllib.parse, urllib.error
import json
import os
import webbrowser
import ssl
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['keys']['api_key']
serviceurl = config['keys']['service_url']

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.txt")
where = open("where.js","w",encoding="utf-8")
adrs=[]

for line in fh:

    address = line.strip()
    parms = dict()
    parms["address"] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    data = urllib.request.urlopen(url, context=ctx).read().decode()

    try:
        js = json.loads(data)
    except:
        print(data)
        continue

    try:
        adrs.append([js['results'][0]['geometry']['lat'],js['results'][0]['geometry']['lng'],js['results'][0]['formatted']])
        print('Retrieved ', url)
    except:
        print("Not Found " + line.strip())

print("\n\nOpening Webpage")

where.write("myData = [\n")
for item in adrs:
    st="[" + str(item[0]) + ", " + str(item[1]) + ", '" + str(item[2]) + "' ], \n"
    where.write(st)
    where.write(",\n")
where.write("];\n")

webbrowser.open('file://' + os.path.realpath("index.html"))