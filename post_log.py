import json
import requests
import pprint

url='https://localhost:5000/api/logic/4'
auth=('beadmin','BEadmin123')

params={'depth':1}

payload=json.loads('{"name":"LOG_30","programs":[{"name":"program_0","flows":[{"type":"fe.shape.InputFigure","id":"1aa57aac-465b-f931-bfb9-5e35db09f1cc","x":393,"y":58,"width":211.875,"height":28,"alpha":1,"userData":{"property":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d","from":"entity_property_name","entity_property_name":"p1"},"cssClass":"Point Write","ports":[{"type":"draw2d.InputPort","id":"0678ffd7-5db7-29cd-43e2-5a2b08f85ecd","width":10,"height":10,"alpha":1,"userData":{"__node__":"1aa57aac-465b-f931-bfb9-5e35db09f1cc","__name__":"property"},"cssClass":"draw2d_InputPort input-port-connected","bgColor":"#08161D","color":"#00E7E8","stroke":1,"maxFanOut":1,"name":"1aa57aac-465b-f931-bfb9-5e35db09f1cc_input_port_17d77a67-f01f-dea8-8f95-2d304365ba39","port":"draw2d.InputPort","locator":"draw2d.layout.locator.InputPortLocator"}],"bgColor":"#08161D","color":"#6A787F","stroke":1,"radius":16,"name":"Point Write"},{"type":"fe.shape.InputOutputFigure","id":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d","x":202,"y":25,"width":140,"height":88,"alpha":1,"userData":{"normal input":"802d954b-b5dc-438c-b28c-ec76a3dcbf3f","switch":"553efe42-24e9-24c6-8176-b058c2e9be9a","alt input":"a76b8d35-cfa5-8de4-c048-4ef0765e235a"},"cssClass":"Switch","ports":[{"type":"draw2d.OutputPort","id":"f2ce8527-581b-2df5-6ada-fc6441891df6","width":10,"height":10,"alpha":1,"userData":{"__node__":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d","__name__":"output"},"cssClass":"draw2d_OutputPort output-port-connected","bgColor":"#08161D","color":"#0DDF6D","stroke":1,"maxFanOut":9007199254740991,"name":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d_output_port_12baf401-16ea-060b-289c-02d94f1dbc08","port":"draw2d.OutputPort","locator":"draw2d.layout.locator.OutputPortLocator"},{"type":"draw2d.InputPort","id":"97194449-fae3-f149-db19-eac077172558","width":10,"height":10,"alpha":1,"userData":{"__node__":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d","__name__":"normal input"},"cssClass":"draw2d_InputPort input-port-connected","bgColor":"#08161D","color":"#00E7E8","stroke":1,"maxFanOut":1,"name":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d_input_port_1bdb632d-3821-715d-f836-4d3763ffc0b9","port":"draw2d.InputPort","locator":"draw2d.layout.locator.InputPortLocator"},{"type":"draw2d.InputPort","id":"d6541435-c513-f3d7-82b1-b3d30037790e","width":10,"height":10,"alpha":1,"userData":{"__node__":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d","__name__":"alt input"},"cssClass":"draw2d_InputPort input-port-connected","bgColor":"#08161D","color":"#00E7E8","stroke":1,"maxFanOut":1,"name":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d_input_port_8d95347a-bf6c-24f3-2c3e-3ed9f9f133bf","port":"draw2d.InputPort","locator":"draw2d.layout.locator.InputPortLocator"},{"type":"draw2d.InputPort","id":"fdd6857c-2821-53c1-05f2-222615b1f87d","width":10,"height":10,"alpha":1,"userData":{"__node__":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d","__name__":"switch"},"cssClass":"draw2d_InputPort input-port-connected","bgColor":"#08161D","color":"#00E7E8","stroke":1,"maxFanOut":1,"name":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d_input_port_da881b78-7470-b308-85f6-603ef3dffba8","port":"draw2d.InputPort","locator":"draw2d.layout.locator.InputPortLocator"}],"bgColor":"#08161D","color":"#6A787F","stroke":1,"radius":16,"name":"Switch"},{"type":"fe.shape.OutputFigure","id":"802d954b-b5dc-438c-b28c-ec76a3dcbf3f","x":20,"y":20,"width":100,"height":28,"alpha":1,"userData":{"from":"value","value":8},"cssClass":"Analog Constant","ports":[{"type":"draw2d.OutputPort","id":"ee41a673-e9ac-82bf-2d1d-10f77dc4b969","width":10,"height":10,"alpha":1,"userData":{"__node__":"802d954b-b5dc-438c-b28c-ec76a3dcbf3f","__name__":"output"},"cssClass":"draw2d_OutputPort output-port-connected","bgColor":"#08161D","color":"#0DDF6D","stroke":1,"maxFanOut":9007199254740991,"name":"802d954b-b5dc-438c-b28c-ec76a3dcbf3f_output_port_10945e74-cd6d-b11a-a71e-77d224d8c8cb","port":"draw2d.OutputPort","locator":"draw2d.layout.locator.OutputPortLocator"}],"bgColor":"#08161D","color":"#6A787F","stroke":1,"radius":16,"name":"Analog Constant"},{"type":"fe.shape.OutputFigure","id":"a76b8d35-cfa5-8de4-c048-4ef0765e235a","x":20,"y":85,"width":100,"height":28,"alpha":1,"userData":{"from":"value","value":8},"cssClass":"Analog Constant","ports":[{"type":"draw2d.OutputPort","id":"2b0fb96a-9d01-a434-3dff-99b041c0f3f4","width":10,"height":10,"alpha":1,"userData":{"__node__":"a76b8d35-cfa5-8de4-c048-4ef0765e235a","__name__":"output"},"cssClass":"draw2d_OutputPort output-port-connected","bgColor":"#08161D","color":"#0DDF6D","stroke":1,"maxFanOut":9007199254740991,"name":"a76b8d35-cfa5-8de4-c048-4ef0765e235a_output_port_7037796a-4441-c672-5d1c-b31bb882f0da","port":"draw2d.OutputPort","locator":"draw2d.layout.locator.OutputPortLocator"}],"bgColor":"#08161D","color":"#6A787F","stroke":1,"radius":16,"name":"Analog Constant"},{"type":"fe.shape.OutputFigure","id":"553efe42-24e9-24c6-8176-b058c2e9be9a","x":109,"y":151,"width":100,"height":28,"alpha":1,"userData":{"from":"value","value":8},"cssClass":"Analog Constant","ports":[{"type":"draw2d.OutputPort","id":"525b6eef-e0f8-5777-1a67-68b8fdbb494b","width":10,"height":10,"alpha":1,"userData":{"__node__":"553efe42-24e9-24c6-8176-b058c2e9be9a","__name__":"output"},"cssClass":"draw2d_OutputPort output-port-connected","bgColor":"#08161D","color":"#0DDF6D","stroke":1,"maxFanOut":9007199254740991,"name":"553efe42-24e9-24c6-8176-b058c2e9be9a_output_port_9c3e884e-10bd-4633-8af5-090bd5e24cb1","port":"draw2d.OutputPort","locator":"draw2d.layout.locator.OutputPortLocator"}],"bgColor":"#08161D","color":"#6A787F","stroke":1,"radius":16,"name":"Analog Constant"},{"type":"draw2d.Connection","id":"1da15a7a-b403-fb55-a111-a6f0c40db481","alpha":1,"userData":{},"cssClass":"draw2d_Connection","stroke":3,"color":"#0DDF6D","outlineStroke":1,"outlineColor":"#0DDF6D","policy":"draw2d.policy.line.LineSelectionFeedbackPolicy","router":"draw2d.layout.connection.SplineConnectionRouter","radius":5,"source":{"node":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d","port":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d_output_port_12baf401-16ea-060b-289c-02d94f1dbc08"},"target":{"node":"1aa57aac-465b-f931-bfb9-5e35db09f1cc","port":"1aa57aac-465b-f931-bfb9-5e35db09f1cc_input_port_17d77a67-f01f-dea8-8f95-2d304365ba39"}},{"type":"draw2d.Connection","id":"b5ffeead-23cb-ffbb-0e76-f4aa40b0b776","alpha":1,"userData":{},"cssClass":"draw2d_Connection","stroke":3,"color":"#0DDF6D","outlineStroke":1,"outlineColor":"#0DDF6D","policy":"draw2d.policy.line.LineSelectionFeedbackPolicy","router":"draw2d.layout.connection.SplineConnectionRouter","radius":5,"source":{"node":"802d954b-b5dc-438c-b28c-ec76a3dcbf3f","port":"802d954b-b5dc-438c-b28c-ec76a3dcbf3f_output_port_10945e74-cd6d-b11a-a71e-77d224d8c8cb"},"target":{"node":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d","port":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d_input_port_1bdb632d-3821-715d-f836-4d3763ffc0b9"}},{"type":"draw2d.Connection","id":"9c718c6e-4a26-d458-d442-71562c35dd96","alpha":1,"userData":{},"cssClass":"draw2d_Connection","stroke":3,"color":"#0DDF6D","outlineStroke":1,"outlineColor":"#0DDF6D","policy":"draw2d.policy.line.LineSelectionFeedbackPolicy","router":"draw2d.layout.connection.SplineConnectionRouter","radius":5,"source":{"node":"a76b8d35-cfa5-8de4-c048-4ef0765e235a","port":"a76b8d35-cfa5-8de4-c048-4ef0765e235a_output_port_7037796a-4441-c672-5d1c-b31bb882f0da"},"target":{"node":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d","port":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d_input_port_8d95347a-bf6c-24f3-2c3e-3ed9f9f133bf"}},{"type":"draw2d.Connection","id":"90522079-dc10-2e9b-865f-90e5904d7ae7","alpha":1,"userData":{},"cssClass":"draw2d_Connection","stroke":3,"color":"#0DDF6D","outlineStroke":1,"outlineColor":"#0DDF6D","policy":"draw2d.policy.line.LineSelectionFeedbackPolicy","router":"draw2d.layout.connection.SplineConnectionRouter","radius":5,"source":{"node":"553efe42-24e9-24c6-8176-b058c2e9be9a","port":"553efe42-24e9-24c6-8176-b058c2e9be9a_output_port_9c3e884e-10bd-4633-8af5-090bd5e24cb1"},"target":{"node":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d","port":"b3f04671-b72d-fa8d-3ea2-3ad951a4194d_input_port_da881b78-7470-b308-85f6-603ef3dffba8"}}]}],"class":"brightedge.services.logic.models.Logic","comments":[],"linked_entities":[],"id":4}") 

resp = requests.put(url, auth=auth, params=params, verify=False, json=payload)
pprint.pprint(resp.json())