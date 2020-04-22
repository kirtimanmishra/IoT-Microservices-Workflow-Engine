# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 00:00:51 2020

@author: KIRTIMAN
"""
import requests

while 1:
    node_url = 'http://localhost:5000/wfe/wf/process'
    response1=requests.post(node_url)
    print('response',response1)
