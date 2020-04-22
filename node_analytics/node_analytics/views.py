from datetime import datetime
from flask import render_template
from node_analytics import app
from flask import Flask, redirect, url_for, request, render_template, jsonify, Response
import pandas as pd
import requests
import os, sys
from importlib import import_module
import json
import cv2
import base64
import numpy as np
import ast
from PIL import Image
face_cascade = cv2.CascadeClassifier('D:/Projects/IoT Project/FlaskWebProject1/FlaskWebProject1/haarcascade_frontalface_default.xml')

@app.route('/node_analytics',methods = ['GET','POST'])
def ProcessImage():
    if(request.method == 'POST'):
        jsonData = request.json
        wfID = jsonData['wfID']
        nodeID = jsonData['nodeID']
        jsonData['status']='pending'
        img_path=jsonData['img_path']
        image = cv2.imread(img_path)
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grayImage)    
        #print(type(faces))
        if len(faces) == 0:
            print('Faces are')
            print("No faces found")
            jsonData['count_faces'] = 0
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
            jsonData['count_faces'] = faces.shape[0] 
            print('Faces are')
            print(faces.shape[0])
        jsonData['nodeID']='node_analytics'
        print(wfID,"+",nodeID)
        url = 'http://localhost:5010/wfEngine/submit'
        response=requests.post(url, json=jsonData)
        print('response',response)
        return 'Images Processed'
    else:
        return 'Please Let The Workflow Begin'

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
