from flask import Flask, request, jsonify, render_template
from Wf_Engine import app
import os, sys
from importlib import import_module
import pandas as pd
import requests


conditionsBaseFolder= 'D:\Projects\IoT Workflow\FlaskWebProject1\FlaskWebProject1\Conditions' 
log_file_path = 'D:\Projects\IoT Workflow\FlaskWebProject1\FlaskWebProject1\Conditions\logs\wf_log.csv'
sys.path.append(conditionsBaseFolder)

@app.route('/')
@app.route('/home')
@app.route('/wfConditions/reload/<module>')
def conditionsReload(module):
    moduleName = import_module("wf_conditions."+module)
    reload(moduleName)
    return "vamsi"

@app.route('/wfEngine/submit',methods = ['GET','POST'])
def wf_submit() :
    if(request.method == 'GET'):
        nodeID = request.args.get("nodeID")
        wfID = request.args.get("wfID")
        store_log(wfID,nodeID,'processed')
        print('Log stored')
        print('Workflow Finished')
        return 'Workflow finished'
    jsonData = request.json
    wfID = jsonData['wfID']
    nodeID = jsonData['nodeID']
    store_log(wfID,nodeID,'processed')
    print('Log stored')
    print("In Central Engine. Received from "+nodeID)
    conditionsModule = import_module("wf_conditions."+wfID)
    targetNodes = conditionsModule.conditionHandler(jsonData,nodeID)
    print('wf_conditions accessed. Target(s) acquired.')
    headers = {'Content-type': 'application/json'}
    for nodeURL in targetNodes:
        requests.post(url = nodeURL,json = jsonData, headers=headers)
    print('Sent to next Node(s)')
    resp = jsonify(success=True)
    return resp
    
@app.route('/wfEngine/display_log', methods=['GET'])
def display_log():
    if(os.path.exists(log_file_path)):
        workflow_log = pd.read_csv(log_file_path)
        return render_template('display_log.html',mydf=workflow_log)
    else:
        return 'No Log found'

def store_log(wfID, nodeID, status):
    workflow_log = None
    if(os.path.exists(log_file_path)):
        workflow_log = pd.read_csv(log_file_path)
    else:
        workflow_log = pd.DataFrame(columns=['wfID','nodeID','status'])
    data = {'wfID':wfID, 'nodeID':nodeID, 'status':status}
    workflow_log = workflow_log.append(data, ignore_index=True)
    workflow_log.to_csv(log_file_path, index=False)


@app.route('/wfEngine/clear_log', methods=['GET'])
def clear_log():
    if(os.path.exists(log_file_path)):
        os.remove(log_file_path)
    resp = jsonify(success=True)
    return resp