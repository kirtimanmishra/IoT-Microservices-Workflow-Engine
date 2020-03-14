# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:39:04 2020

@author: KIRTIMAN
"""

def process():
    {'wf1':[ lambda x : 'node1' if x['wfid']=='wf1' and x['status']=='pending'
        else '0000', lambda x : 'node100' if x['wfid']=='wf1' and x['status']=='processed' else '0000' ] }

    {'wf2':[ lambda x : 'node2' if x['wfid']=='wf2' and x['status']=='pending' 
        else '0000', lambda x : 'node200' if x['wfid']=='wf2' and x['status']=='processed' else '0000' ]}

def show():
    print('kirti')