#----  REST api to get the history of the points under a single device

import requests
import pprint

url='https://www.hipchat.com/sign_in'
uris="['/AI/p1','/AI/p2','/AI/p3']"
auth=('beadmin','BEadmin123')


params={ 'uris':uris, 'start':"2015-07-01", 'end':"2018-07-01"}

#params={ 'uris':uris, "end":"2018-07-01"}

resp = requests.get(url, auth=auth, params=params, verify=False)
pprint.pprint(resp.json())

