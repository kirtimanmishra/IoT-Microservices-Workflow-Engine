# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:52:09 2020

@author: KIRTIMAN
"""
def conditionHandler(values,currNode):
    if(currNode=='node_camera'):
        return ['http://localhost:5002/node_analytics']
    if(currNode=='node_analytics' and values['count_faces']>=10):
        return ['http://localhost:5004/node_AC']
    if(currNode=='node_analytics' and values['count_faces']<10):
        return ['http://localhost:5003/node_ignore']