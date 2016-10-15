#! python2
# riesal@gmail.com

# default resell.biz output for getting promo prices is include the keys id
# which is getting hard for us to quickly search what domain is still in
# promotion and the details.
# so i begin to download, and delete the first element(which is the unused key)
# and save the result in append mode.

# todo:
# format result as restful, not file

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
