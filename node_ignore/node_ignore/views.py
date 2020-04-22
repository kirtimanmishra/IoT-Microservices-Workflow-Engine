from datetime import datetime
from flask import render_template
from node_ignore import app
import requests
from flask import Flask, redirect, url_for, request, render_template, jsonify, Response
import pandas as pd
import os, sys
from importlib import import_module

@app.route('/node_ignore',methods = ['GET','POST'])
def GetIgnoreIoTData():
    if(request.method == 'POST'):
        jsonData = request.json
        wfID = jsonData['wfID']
        msgid = jsonData['msgid']
        jsonData['nodeID']='node_ignore'
        jsonData['status']='processed'
        paramData={'nodeID':'node_ignore', 'wfID':wfID, 'msgid':msgid, 'status': 'processed'}
        url = 'http://localhost:5010/wfEngine/submit'
        response = requests.get(url, params=paramData)
        print('Connecting To IoT')
        print("Curresponding Meggage Id:"+msgid)
        print('response',response)
        print('Turning OFF AC')
        return 'Turning OFF AC'

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
