"""
Created on Sat Feb 22 22:17:02 2020

@author: KIRTIMAN
"""
from __future__ import print_function
import requests
import json
import cv2
import os
import base64
import numpy as np
import ast
from PIL import Image
face_cascade = cv2.CascadeClassifier('D:/Projects/IoT Project/FlaskWebProject1/FlaskWebProject1/haarcascade_frontalface_default.xml')


with open('buffer.json') as f:
    content = f.readlines()
list = [ ast.literal_eval( line ) for line in content ]

for i in range(len(list)):
    url = 'http://localhost:5000/wfe/wf/submit'
    dict={}
    dict=list[i]
    path=dict['img_path']
    msgid=dict['msgid']
    image = cv2.imread(path)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayImage)    
    print(type(faces))
    if len(faces) == 0:
        print("No faces found")
        dict['count_faces'] = 0
    else:
        #print(faces)
        print(faces.shape)
        print("Number of faces detected: " + str(faces.shape[0]))
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
        cv2.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
        cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
        #cv2.imshow('Image with faces',image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        dict['count_faces'] = faces.shape[0]    
    dict['wfid'] = 'wf_ANALYTICS'
    dict['node'] = 'node_analytics'
    print(dict)
    print(msgid)
    node_url = 'http://localhost:5000/wfe/node/process/msg{0}'.format(i+1)
    response=requests.post(url, json=dict)
    response1=requests.post(node_url)
    print('response',response)
    print('response',response1)
    #break
    #img.show()
    
    
    