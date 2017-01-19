#---- POST api in json format into postman

import json
import requests
import pprint

url='http://127.0.0.1:5000/auth/1/login'
#auth=()

payload = "{\"mobileno\": \"9945416327\", \"passwd\": \"mypassword\", \"otp\": \"731221\"}"

headers = {'content-type': "application/json"}

resp = requests.post(url, data=payload, headers=headers, verify=True)

pprint.pprint(resp.text)


