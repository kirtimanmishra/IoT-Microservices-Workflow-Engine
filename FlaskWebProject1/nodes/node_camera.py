"""
Created on Tue Feb 11 14:11:54 2020

@author: KIRTIMAN
"""
from __future__ import print_function
import requests
import json
import cv2
import os
import base64
import numpy as np
from PIL import Image

base_dir = 'D:/Projects/IoT Project/FlaskWebProject1/FlaskWebProject1/nodes'
cam_dir = base_dir+'/node_camera/'
to_dir = base_dir+'/node_analytics/'
i=0
listing = os.listdir(cam_dir)
for file in listing:
    print(len(file))
    url = 'http://localhost:5000/wfe/wf/submit'
    #imageFile = Image.open(cam_dir + file) 
    imageFile = open(cam_dir + file,'rb')  
    msgid='msg'+str(i+1)
    #img = base64.b64encode(imageFile.read())
    #print(len(img))
    myobj = {'wfid': 'wf_CAM_AC', 
             'node':'node_camera',
             'status':'pending',
             'img_path':cam_dir+file,
             'count_faces':'NONE',
             'msgid':msgid
             }
    i=i+1
    node_url = 'http://localhost:5000/wfe/node/process/msg{0}'.format(i)
    response=requests.post(url, json=myobj)
    response1=requests.post(node_url)
    #response=requests.post(url, data=myobj)
    print('response',response)
    print('response',response1)
    #break