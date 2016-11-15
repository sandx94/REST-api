import json
import requests
import pprint

url='https://localhost:5000/api/entities/Site/grp2/dev20/properties/AV/New%20Point'
auth=('beadmin','BEadmin123')

params={'depth':1}

payload=json.loads('{"name":"p747","obj_type":"Test Analog Output","tags":[{"name":"dis","kind":"Str","value":""},{"name":"siteRef","kind":"Ref","value":"84caa6c8-71ec-448f-a48a-88f48422bdd7"}],"uri":"/Site/grp2/dev20/properties/AI/p10","ptype":"AI","at_limit":"oscillate","category":"random","valid_lower":"50","valid_upper":"80","step":"1","init_value":"50","outlier_upper":"100","outlier_lower":"30","outlier_upper_init_value":"100","outlier_lower_init_value":"50","outlier_category":"random","regen_rate":"1","outlier_balance":".5","read_fail_rate":"0","write_fail_rate":"0","precision":"2","outlier_upper_rate":"0","outlier_lower_rate":"0","hist":true,"freq":30,"protourl":"testproto://sys/dev/AI-point100?category=random&valid_lower=50&valid_upper=80&at_limit=oscillate&step=1&init_value=50&outlier_upper=100&outlier_lower=30&outlier_upper_init_value=100&outlier_lower_init_value=50&outlier_category=random&regen_rate=1&outlier_balance=.5&read_fail_rate=0&write_fail_rate=0&precision=2&float=&outlier_upper_rate=0&outlier_lower_rate=0","alarm":{"tags":["category:general"],"conditions":[],"properties":{}},"instance":"100"}')

resp = requests.put(url, auth=auth, params=params, verify=False, json=payload)
pprint.pprint(resp.json())
