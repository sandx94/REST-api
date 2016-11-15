import requests
import pprint
import json
url= 'https://localhost:5000/api/entities/Site/dev1'
auth=('beadmin','BEadmin123')

params={ 'depth':1}

#---- D W A ----
#resp = requests.get(url, auth=auth, params=params, verify=False)
resp = requests.delete(url, auth=auth, params=params, verify=False)
#print resp
#print resp.text
print "-----------------"
print resp.status_code
print "-----------------"
print dir(resp)
pprint.pprint(resp.json())
