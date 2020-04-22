from datetime import datetime
from flask import render_template
from Wf_Engine import app
from flask import Flask, redirect, url_for, request, render_template, Response
from flask import Flask, request, jsonify, render_template
import pandas as pd
import requests
import os, sys
from importlib import import_module

conditionsBaseFolder= 'D:\Projects\IoT Workflow\FlaskWebProject1\FlaskWebProject1\Conditions' 
log_file_path = 'D:\Projects\IoT Workflow\FlaskWebProject1\FlaskWebProject1\Conditions\logs\wf_log.csv'
sys.path.append(conditionsBaseFolder)

@app.route('/wfEngine/submit',methods = ['GET','POST'])
def wf_submit() :
    if(request.method == 'GET'):
        nodeID = request.args.get("nodeID")
        wfID = request.args.get("wfID")
        msgid = request.args.get("msgid")
        print("Last Node's Data: ")
        print(nodeID)
        print(wfID)
        print(msgid)
        #store_log(wfID,nodeID,'processed')
        print('Log stored')
        print('Workflow Finished Or Not Started')
        return 'Workflow finished'
    if(request.method == 'POST'):
        jsonData = request.json
        wfID = jsonData['wfID']
        nodeID = jsonData['nodeID']
        jsonData['status']='processed'
        print(wfID,"+",nodeID)
        #store_log(wfID,nodeID,'processed')
        #print('Log stored')
        print("In Central Engine. Received from "+nodeID)
        conditionsModule = import_module("wf_conditions."+wfID)
        targetNodes = conditionsModule.conditionHandler(jsonData,nodeID)
        print('wf_conditions accessed. Target(s) acquired.')
        headers = {'Content-type': 'application/json'}
        for nodeURL in targetNodes:
            print(nodeURL)
            response = requests.post(url = nodeURL,json = jsonData, headers=headers)
            print(response)
        print('Sent to next Node(s)')
        resp = jsonify(success=True)
        return resp
    return 'Workflow Processed'
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
