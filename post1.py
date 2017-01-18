#---- POST api in json format into postman

import json
import requests
import pprint

url='http://127.0.0.1:5000/auth/1/login'
#auth=()

params={"mobileno":"9945416327", "passwd":"mypassword", "otp":"731221"}

resp = requests.post(url, params=params, verify=True)
print resp.text
#pprint.pprint(resp.text)


