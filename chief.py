#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:42:15 2017

@author: kshitijbhatnagar
"""


from flask import Flask
from flask_restful import Resource, Api, reqparse
import json, requests, time, getpass

class chiefServer():
    def __init__(self):
        self.secondary=input("Enter the total number of secondary nodes: ")
        # Conbert it into int
        self.secondary=int(self.secondary)
        #set the timer to zero
        self.starttime=0.0
        #current number of secondary connected to manger
        self.currentsecondary= 0
        currentpage=1
        nextpage=True
        #commit list to store SHA values
        self.commitlist=[]
        while nextpage:
            
            r=requests.get("https://github.com/bhatnagark/Scaleable-Computing-ChatBot")
            json_data=json.loads(r.text)
            
            if len(json_data)<2:
                nextpage-= False
                print("All pages are done")
                
            else:
                for x in json_data:
                    self.commitlist.append(x['sha'])
                    print("sha:{}".format(x['sha']))
                currentpage+=1 
        self.totalcommits=len(self.commitlist)
        self.listofccs=[]
        print("Number of commits: {}".format(self.totalNumberOfCommits))        
                
                                
            
            
        
    


if __name__ == "__main__":
    chiedS = chiefServer()  # ini an instance of managerServer()
    app.run(port=9000)