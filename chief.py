#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:42:15 2017

@author: kshitijbhatnagar
"""


from flask import Flask
from flask_restful import Resource, Api, reqparse
import json, requests, time, getpass

class repository:
    def __init__(self):
        #global server object
        global chiefS
        self.server = chiefS
        super(repository,self).__init__()
        self.reqparser = reqparser.RequestParser()
        
        self.reqparser.add_argument('pullStatus', type=int, location = 'json')
        self.reqparser.add_argument('complexity', type=float, location = 'json')
        
        
    def get(self):
        args=self.reqparser.parse_args()
        #repo has not been pulled yet 
        if args['pullStatus'] == False:
            print("Got")
            return {'repo':"https://github.com/bhatnagark/Scaleable-Computing-ChatBot"}
        
        if args['pullStatus'] == True:
            self.server.currentsecondary +=1
            if self.server.currentsecondary == self.server.secondary:
                #start time
                self.server.starttime=time.time()
            print("WORKER NUMBER: {}".format(self.server.currentsecondary))
            
    def post(self):
        pass
    
 api.add_resource(repository, "/repo", endpoint="repo") 

  
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
    chiefS = chiefServer()  # ini an instance of managerServer()
    app.run(port=9000)