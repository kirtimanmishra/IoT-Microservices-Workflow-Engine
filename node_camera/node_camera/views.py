from datetime import datetime
from flask import render_template
from node_camera import app
from flask import Flask, redirect, url_for, request, render_template, Response
from flask import Flask, request, jsonify, render_template
import pandas as pd
import requests
import os, sys
from importlib import import_module

cam_dir = 'D:/Projects/IoT Workflow/FlaskWebProject1/FlaskWebProject1/nodes/node_camera/'

@app.route('/node_camera')
def GetImagePath():
    i=0
    listing = os.listdir(cam_dir)
    for file in listing:
        #print(len(file))
        url = 'http://localhost:5010/wfEngine/submit'
        #imageFile = Image.open(cam_dir + file) 
        imageFile = open(cam_dir + file,'rb')  
        msgid='msg'+str(i+1)
        #img = base64.b64encode(imageFile.read())
        #print(len(img))
        myobj = {'wfID': 'wf_AC', 
                 'nodeID':'node_camera',
                 'status':'pending',
                 'img_path':cam_dir+file,
                 'count_faces':'NONE',
                 'msgid':msgid
                 }
        i=i+1
        response=requests.post(url, json=myobj)
        print('response',response)
        #break
    return 'Images Loaded'










@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
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


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )