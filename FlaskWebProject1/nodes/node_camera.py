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
    #img = base64.b64encode(imageFile.read())
    #print(len(img))
    myobj = {'wfid': 'wf_CAM_AC', 
             'node':'node_camera',
             'status':'pending',
             'img_path':cam_dir+file,
             'count_faces':'NONE',
             'msgid':'msg'+str(i+1)
             }
    i=i+1
    response=requests.post(url, json=myobj)
    #response=requests.post(url, data=myobj)
    print('response',response)
    #break