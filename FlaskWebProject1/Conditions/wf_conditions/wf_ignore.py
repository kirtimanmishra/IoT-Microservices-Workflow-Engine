# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:39:04 2020

@author: KIRTIMAN
"""
def conditionHandler(values,currNode):
    if(currNode=='node_camera'):
        return ['http://localhost:5002/node_analytics']
    if(currNode=='node_analytics' and values['count_faces']<10):
        return ['http://localhost:5003/node_ignore']