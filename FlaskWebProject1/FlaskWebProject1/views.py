"""
The codes are copyrighted to Dr. Kalidas Yeturu of IIT Tirupati. 2019/Nov/28. Please contact him at ykalidas@iittp.ac.in for permission to use these codes.
The codes are not to be distributed or used without prior permission.
The author is not liable for any damage incurred by the user of these codes.
"""

from datetime import datetime
from FlaskWebProject1 import app
from flask import Flask, redirect, url_for, request, render_template
from flask import Flask, redirect, url_for, request, render_template, Response
import jsonpickle
import numpy as np
import requests
import pandas as pd
from FlaskWebProject1.workflow import WFE
import shutil  
from PIL import Image
import cv2
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import base64
import binascii
import time
#import conditions
#import conditions_python
import pandas as pd
from FlaskWebProject1.workflow import WFE

condn_file = 'D:/Projects/IoT Project/FlaskWebProject1/FlaskWebProject1/wf_conditions.txt' 
#condn_file = 'D:/Projects/IoT Project/FlaskWebProject1/FlaskWebProject1/conditions_python.pyc' 
#condn_file = str(conditions_python.conditions())
condhand = WFE.ConditionHandler(condn_file)
wflog = WFE.WFLog()
nodelog = WFE.NodeLog()
wflog.setnodelog(nodelog)
wflog.sethandler(condhand)
nodelog.setwflog(wflog)

@app.route('/wfe/wf/submit',methods = ['POST', 'GET'])
def wf_submit() :
    global wflog
    if request.method == 'POST':            
        values = request.json
        mydata = {}
        data = {}
        #camera_dir={}
        dateTimeObj = datetime.now()
        #timeStr = dateTimeObj.strftime("%H:%M:%S.%f")
        mydata['wfid'] = values['wfid']
        mydata['status'] = values['status']
        mydata['node'] = values['node']  
        mydata['count_faces'] = values['count_faces'] 
        mydata['msgid'] = values['msgid'] 
        img_path = values['img_path']
        #data = values['data']
        #print(data)
        #img_path = data['img_path']
        #type = data['type']
        mydata['img_path'] = img_path
        d=os.getcwd()
        d1 = os.path.join(d,"nodes")
        fname = os.path.join(d1,"my_camera.json") 
        f = open(fname,"a+");
        f.write(str(mydata)+"\n")
        wflog.submit(mydata)
        return 'success: POST wf submit'
    else:
        mydata = {}
        mydata['wfid'] = request.args.get('wfid')
        mydata['status'] = 'pending'
        mydata['node'] = request.args.get('node')
        mydata['data'] = request.args.get('data')
        wflog.submit(mydata)
        return 'success: GET wf submit'

@app.route('/wfe/wf/process',methods=['GET'])
def wf_process() :
    global wflog

    wflog.process()

    return 'success: GET wf process'

"""
The codes are copyrighted to Dr. Kalidas Yeturu of IIT Tirupati. 2019/Nov/28. Please contact him at ykalidas@iittp.ac.in for permission to use these codes.
The codes are not to be distributed or used without prior permission.
The author is not liable for any damage incurred by the user of these codes.
"""

@app.route('/wfe/wf/condition',methods=['GET'])
def wf_conditions() :
    condhand.refresh()
    return 'success: GET conditions loadeded'

@app.route('/wfe/node/submit',methods = ['POST', 'GET'])
def node_submit() :
    global nodelog
    if request.method == 'POST':
        values = request.json
        mydata = {}
        mydata['wfid'] = values['wfid']
        mydata['status'] = values['status']
        mydata['node'] = values['node']  
        mydata['count_faces'] = values['count_faces'] 
        mydata['msgid'] = values['msgid'] 
        #img_path = values['img_path']
        #data = values['data']
        #print(data)
        #img_path = data['img_path']
        #type = data['type']
        #mydata['img_path'] = img_path 
        nodelog.submit(mydata)
        return 'success: POST node submit'
    else:
        mydata = {}
        mydata['wfid'] = request.args.get('wfid')
        mydata['status'] = 'pending'
        mydata['node'] = request.args.get('node')
        mydata['data'] = request.args.get('data')
        nodelog.submit(mydata)
        return 'success: GET node submit'

@app.route('/wfe/node/process/<checker>',methods=['GET'])
def node_process(checker) :
    global nodelog

    nodelog.process(checker)

    return 'success: GET node process'

@app.route('/wfe/display/<mytype>')
def display(mytype) :
    print ('display is hit',mytype)
    mylog = wflog
    if mytype=='node' :
        mylog = nodelog
    
    return render_template('wf_render.html',mydf=mylog.debug_getdf())


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


