import ast
import requests

with open('buffer.json') as f:
    content = f.readlines()
list = [ ast.literal_eval( line ) for line in content ]

for i in range(len(list)):
    dict={}
    dict=list[i]
    count_faces=dict['count_faces']
    wfid=dict['wfid']
    node=dict['node']
    if wfid=='wf_ANALYTICS' and node=='node_analytics' and count_faces>=10:
        msgid=dict['msgid']
        id = int(msgid[3:])
        node_url = 'http://localhost:5000/wfe/node/process/msg{0}'.format(id)
        response1=requests.post(node_url)
        print('response',response1)
        print("Turning ON AC"+"\n"+"Sending information to IoT device")
    else:
        print("Turning OFF AC"+"\n"+"Stop Sending information to IoT device")