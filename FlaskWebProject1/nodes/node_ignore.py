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
    if wfid=='wf_ANALYTICS' and node=='node_analytics' and count_faces<10:
        msgid=dict['msgid']
        id = int(msgid[3:])
        #print(type(id))
        node_url = 'http://localhost:5000/wfe/node/process/msg{0}'.format(id)
        print(id)
        response1=requests.post(node_url)
        print('response',response1)
        print("Do Nothing"+"\n"+"People are less")
        print('response',response1)