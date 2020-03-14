# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:42:21 2020

@author: KIRTIMAN
"""

import requests
import json
import cv2
import os
import base64
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob


base_dir = 'D:/Projects/IoT Flask/FlaskWebProject1/FlaskWebProject1/nodes'
to_dir = base_dir+'/node_analytics'
cam_dir = base_dir+'/node_camera'

Single File Transfer

base_dir = 'D:/Projects/IoT Flask/FlaskWebProject1/FlaskWebProject1/nodes'
cam_dir = base_dir+'/node_camera'
to_dir = base_dir+'/node_analytics'

for i in range(1):
    url = 'http://localhost:5000/wfe/wf/submit'
    imageFile = open('less.jpg','rb')  
    img = base64.b64encode(imageFile.read())
    print(len(img))
    myobj = {'wfid': 'wf_CAM_AC', 'node':'node_camera',
             'type':'less_image', 
             'dir':cam_dir,
             'img':img}
    response=requests.post(url, data=myobj)
    print('response',response)



for file in os.listdir(cam_dir):
    #url = 'http://localhost:5000/wfe/wf/submit'
    imageFile = Image.open(os.path.join(cam_dir, file))
    #imageFile = open(os.path.join(cam_dir, file))
    #imgplot = plt.imshow(imageFile)
    #plt.show()
    img = base64.b64encode(imageFile.read())
    #myobj = {'wfid': 'wf_CAM_AC', 'node':'node_camera',
    #         'type':'less_image', 
    #         'dir':cam_dir,
    #         'img':img}
    #response=requests.post(url, data=myobj)
    #print('response',response)
    #imgplot = plt.imshow(imageFile)
    #plt.show()
        
  
      
#for file in cam_dir:
#    path = os.path.join(cam_dir, file)
#    if os.path.isfile(path):
#        img = Image.open(path)
#        mgplot = plt.imshow(img)
#        plt.show()
    #img = mpimg.imread(os.path.join(cam_dir, file))
    #imgplot = plt.imshow(img)
    #plt.show() 

