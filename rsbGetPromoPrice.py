#! python2
# riesal@gmail.com

import requests, json

response = requests.get("https://test.httpapi.com/api/resellers/promo-details.json?auth-userid=your-reseller-id&api-key=your-key")
response.raise_for_status()
ambil = json.loads(response.text)

with open('test3.txt', 'a') as tulis_file:
    for key, value in ambil.iteritems():
        tulis_file.write("{}\n".format(json.dumps(value)))

#no need to open file, read directly from url
#with open('test.txt', 'r') as baca_file:
#    for line in baca_file:
#        data = json.loads(line)

#with open('test2.txt', 'a') as tulis_file:
#    for key, value in data.iteritems():
#        tulis_file.write("{}\n".format(json.dumps(value)))

#for key, value in data.iteritems():
#    print value
#
