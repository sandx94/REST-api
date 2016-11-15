import requests
import pprint
import json
url='https://localhost:5000/api/entities/Site/dev1/properties/AI/p171?depth=1'

auth=('beadmin','BEadmin123')

payload={"protourl":"testproto://sys/dev/AI-point1720?category=random&valid_lower=50&valid_upper=80&at_limit=oscillate&step=1&init_value=50&outlier_upper=100&outlier_lower=30&outlier_upper_init_value=100&outlier_lower_init_value=50&outlier_category=random&regen_rate=1&outlier_balance=.5&read_fail_rate=0&write_fail_rate=0&precision=2&float=false&outlier_upper_rate=0&outlier_lower_rate=0","tags":[{"kind":"Str","name":"dis","value":"sandeep"},{"kind":"Marker","name":"his","value":None},{"kind":"Ref","name":"siteRef","value":"715dfc30-bb5d-40b9-8641-6308fea40f1a"}],"ptype":"AI","propid":"/AI/p171","class":"brightedge.services.entity.core.EntityProperty","freq":30,"id":"/Site/dev1/properties/AI/p171","uuid":"1cf6d853-3ede-4890-9db5-a5c1749792f2","obj_type":"Test Analog Input","name":"p171","alarm":{"uuid":"90597dec-9226-43cc-af87-95e7dd134803","triggered":False,"tags":["category:general"],"transitioned_on":None,"acknowledged":False,"state":"inactive","summary":"","property_uuid":"1cf6d853-3ede-4890-9db5-a5c1749792f2","created_on":1470658597,"updated_on":1470658597,"conditions":[],"properties":{},"trigger_condition":None},"uri":"/Site/dev1/properties/AI/p171","hist":True,"site_uuid":"715dfc30-bb5d-40b9-8641-6308fea40f1a","instance":"1720","category":"random","valid_lower":"50","valid_upper":"80","at_limit":"oscillate","step":"1","init_value":"50","outlier_upper":"100","outlier_lower":"30","outlier_upper_init_value":"100","outlier_lower_init_value":"50","outlier_category":"random","regen_rate":"1","outlier_balance":".5","read_fail_rate":"0","write_fail_rate":"0","precision":"2","float":False,"outlier_upper_rate":"0","outlier_lower_rate":"0"}

resp = requests.put(url, auth=auth, verify=False, json=payload)
pprint.pprint(resp.json())
