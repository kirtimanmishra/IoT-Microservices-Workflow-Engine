from flask import render_template
from FlaskWebProject1 import app

@app.route('/node/<msg>')
def node(msg):
    """Processes a node message"""
    print ('node msg',msg)
    pass

@app.route('/workflow/<msg>')
def workflow(msg) :
    """Processes a workflow message"""
    pass


