import requests
import pprint

url='https://localhost:5000/api/history'
uris="['/Site/d1/properties/AI/p1','/Site/d1/properties/AI/p2','/Site/d2/properties/AI/p3']"
auth=('beadmin','BEadmin123')


params={ 'uris':uris, 'start':"2015-07-01", 'end':"2018-07-01", 'limit':1, 'reverse':"False"}
#params={ 'uris':uris, "end":"2018-07-01"}


#------D W A------
#resp = requests.get(url, auth=auth, params=params, verify=False)
resp = requests.get(url, auth=auth, params=params, verify=False)
pprint.pprint(resp.json())

