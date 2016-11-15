import pprint
import requests
import json

url='https://localhost:5000/api/history'
uris="['/Site/dev1/properties/AI/p5']"
auth=('beadmin','BEadmin123')


params={ 'uris':uris, 'start':"2016-03-01", "end":"2018-10-01" , 'rollup':"True" }
#params={'uris':uris, 'start':"2015-08-06", 'end':"2017-08-01", 'rollup':"True"}


#------ D - W - A ------
resp = requests.get(url, auth=auth, params=params, verify=False)
#ob = json.loads(resp.text)
ob = resp.json()
pprint.pprint (ob)
#print resp.json()
