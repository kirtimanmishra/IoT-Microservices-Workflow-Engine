from datetime import datetime
from flask import render_template
from node_AC import app
from flask import Flask, redirect, url_for, request, render_template, jsonify, Response
import pandas as pd
import requests
import os, sys
from importlib import import_module

@app.route('/node_AC',methods = ['GET','POST'])
def GetIoTData():
    if(request.method == 'POST'):
        jsonData = request.json
        wfID = jsonData['wfID']
        jsonData['nodeID']='node_AC'
        msgid = jsonData['msgid']
        jsonData['status']='pending'
        url = 'http://localhost:5010/wfEngine/submit'
        response=requests.get(url, json=jsonData)
        msgid = jsonData['msgid']
        print('Connecting To IoT from Node AC')
        print("Curresponding Meggage Id:"+msgid)
        print('response',response)
        print('Turning on AC')
        return 'Turning on AC'

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
