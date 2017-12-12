#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 23:26:06 2017

@author: kshitijbhatnagar
"""

import json, requests, subprocess

def run():
    chiefip=input("Please enter the IP of the chief node")
    chiefPort=input("Please enter the port of chief node")
    completecommit=0
    
    r=request.get("http://{}:{}/repo".format(chiefip,chiefPort), json={'pullStatus': False})
    json_data = json.loads(r.text)
    repoUrl = json_data['repo']
    subprocess.call(["bash", "subInitScript.sh", repoUrl])
    
    r=request.get("http://{}:{}/repo".format(chiefip,chiefPort), json={'pullStatus': True)
        
    
if __name__ == "__main__":
    run()